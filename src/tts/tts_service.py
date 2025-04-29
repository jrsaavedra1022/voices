import os
import json
import numpy as np
import soundfile as sf
from TTS.api import TTS
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

class TTSService:
    def __init__(self):
        self.voice_name = settings.voice
        self.voice_info = self._get_voice_info()
        self.tts = self._load_tts()

    def _get_voice_info(self):
        voices_file = os.path.join(settings.model_dir, "voices.json")
        if not os.path.exists(voices_file):
            logger.error(f"No se encontró voices.json en {settings.model_dir}")
            raise FileNotFoundError("voices.json no encontrado.")

        with open(voices_file, 'r', encoding='utf-8') as f:
            voices = json.load(f)

        if self.voice_name not in voices:
            logger.error(f"La voz '{self.voice_name}' no está registrada en voices.json")
            raise ValueError(f"Voz '{self.voice_name}' no válida.")

        return voices[self.voice_name]

    def _load_tts(self):
        logger.info(f"Cargando modelo TTS para la voz: {self.voice_name}")

        model_folder = os.path.join(settings.model_dir, self.voice_info["model_dir"])

        model_file = os.path.join(model_folder, self.voice_info["model_file"])
        config_file = os.path.join(model_folder, self.voice_info["config_file"])

        if not os.path.exists(model_file) or not os.path.exists(config_file):
            raise FileNotFoundError(f"Faltan archivos necesarios en el modelo: {model_file} o {config_file}")

        return TTS(
            model_path=model_file,
            config_path=config_file,
            progress_bar=True,
            gpu=False
        )

    def generate_audio(self, text: str, output_path: str):
        logger.info(f"Generando audio: {output_path}")

        wav = self.tts.tts(text=text)
        sf.write(output_path, wav, samplerate=self.tts.synthesizer.output_sample_rate)