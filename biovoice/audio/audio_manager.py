import os
from pydub import AudioSegment
from utils.logger import setup_logger

from audio.interfaces.audio_enhancer import IAudioEnhancer
from audio.enhancer.enhancer_service import EnhancerService
from audio.effects.silence_reducer import SilenceReducer
from audio.effects.crossfade_mixer import CrossfadeMixer

logger = setup_logger(__name__)

class AudioManager:
    def __init__(self):
        self.silence_reducer = SilenceReducer()
        self.crossfade_mixer = CrossfadeMixer()
        self.audio_enhancer: IAudioEnhancer = EnhancerService()

    def combine_audios(self, audio_files: list, output_path: str):
        self.crossfade_mixer.mix(audio_files, output_path)

    def enhance_audio(self, input_path: str):
        logger.info(f"Iniciando proceso de mejora en: {input_path}")
        audio = AudioSegment.from_wav(input_path)

        # 1. Reducción de silencios largos
        reduced = self.silence_reducer.reduce(audio)
        reduced.export(input_path, format="wav")

        # 2. Mejora profesional de calidad de audio
        self.audio_enhancer.enhance(input_path)

    def delete_temp_audios(self, audio_files: list):
        for audio_file in audio_files:
            try:
                os.remove(audio_file)
                logger.info(f"Eliminado archivo temporal: {audio_file}")
            except Exception as e:
                logger.error(f"Error al eliminar {audio_file}: {str(e)}")