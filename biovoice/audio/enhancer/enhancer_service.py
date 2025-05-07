# audio/enhancer/enhancer_service.py

import os
import numpy as np
import soundfile as sf
import librosa
import noisereduce as nr

from config.settings import settings
from audio.interfaces.audio_enhancer import IAudioEnhancer
from audio.enhancer.loudness_normalizer import LoudnessNormalizer
from audio.enhancer.rms_compressor import RMSCompressor
from audio.enhancer.bandpass_filter import BandpassFilter
from utils.logger import setup_logger

logger = setup_logger(__name__)

class EnhancerService(IAudioEnhancer):
    def __init__(self):
        self.compressor = RMSCompressor(
            threshold=settings.rms_threshold,
            ratio=settings.rms_ratio
        )
        self.filter = BandpassFilter(
            low_freq=settings.bandpass_low_freq,
            high_freq=settings.bandpass_high_freq
        )
        self.normalizer = LoudnessNormalizer(
            target_lufs=settings.target_lufs
        )

    def enhance(self, input_path: str, output_path: str = None) -> None:
        logger.info(f"Iniciando mejora de audio: {input_path}")

        y, sr = librosa.load(input_path, sr=None)

        # 1. Reducción de ruido
        noise_clip = y[:int(sr * 0.5)]
        y_denoised = nr.reduce_noise(y=y, sr=sr, y_noise=noise_clip, prop_decrease=1.0)

        # 2. Compresión RMS
        y_compressed = self.compressor.compress(y_denoised)

        # 3. Filtro pasa banda
        y_filtered = self.filter.apply(y_compressed, sr)

        # 4. Normalización de amplitud
        y_normalized = librosa.util.normalize(y_filtered)

        # 5. Guardar y aplicar normalización de loudness
        final_path = output_path if output_path else input_path
        sf.write(final_path, y_normalized, sr)
        self.normalizer.normalize(final_path)

        logger.info(f"Mejora finalizada y exportada en: {final_path}")