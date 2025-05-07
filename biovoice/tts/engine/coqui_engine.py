import os
import json
import numpy as np
import soundfile as sf
from TTS.api import TTS
from config.settings import settings
from utils.logger import setup_logger
from tts.interfaces.tts_engine import ITTSEngine

logger = setup_logger(__name__)

class CoquiEngine(ITTSEngine):
    def __init__(self):
        self.voice_name = settings.voice
        self.voice_info = self._get_voice_info()
        self.tts = self._load_tts()

    def _get_voice_info(self):
        voices_file = os.path.join(settings.model_dir, "voices.json")
        if not os.path.exists(voices_file):
            raise FileNotFoundError("voices.json no encontrado en el modelo.")

        with open(voices_file, 'r', encoding='utf-8') as f:
            voices = json.load(f)

        if self.voice_name not in voices:
            raise ValueError(f"Voz '{self.voice_name}' no válida.")

        return voices[self.voice_name]

    def _load_tts(self):
        logger.info(f"Cargando modelo TTS para la voz: {self.voice_name}")
        model_folder = os.path.join(settings.model_dir, self.voice_info["model_dir"])

        model_file = os.path.join(model_folder, self.voice_info["model_file"])
        config_file = os.path.join(model_folder, self.voice_info["config_file"])

        if not os.path.exists(model_file) or not os.path.exists(config_file):
            raise FileNotFoundError("Faltan archivos del modelo TTS.")

        return TTS(
            model_path=model_file,
            config_path=config_file,
            progress_bar=True,
            gpu=False
        )

    def synthesize(self, text: str, output_path: str):
        logger.info(f"Generando audio en: {output_path}")
        wav = self.tts.tts(text=text)
        sf.write(output_path, wav, samplerate=self.tts.synthesizer.output_sample_rate)