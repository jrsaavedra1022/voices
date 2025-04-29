import os
from pydub import AudioSegment
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

class AudioManager:
    def __init__(self):
        self.silence_duration = settings.silence_duration_ms

    def combine_audios(self, audio_files: list, output_path: str):
        combined = AudioSegment.empty()

        for audio_file in audio_files:
            logger.info(f"Agregando audio: {audio_file}")
            audio = AudioSegment.from_wav(audio_file)
            combined += audio + AudioSegment.silent(duration=self.silence_duration)

        logger.info(f"Exportando audio final: {output_path}")
        combined.export(output_path, format="wav")

    def delete_temp_audios(self, audio_files: list):
        for audio_file in audio_files:
            try:
                os.remove(audio_file)
                logger.info(f"Eliminado archivo temporal: {audio_file}")
            except Exception as e:
                logger.error(f"No se pudo eliminar {audio_file}: {str(e)}")