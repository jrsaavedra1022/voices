from pydub import AudioSegment
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

class CrossfadeMixer:
    def __init__(self):
        self.dynamic = settings.crossfade_dynamic
        self.min_ms = settings.crossfade_min_ms
        self.max_ms = settings.crossfade_max_ms
        self.ratio = settings.crossfade_ratio
        self.silence_duration = settings.silence_duration_ms

    def mix(self, audio_files: list, output_path: str):
        logger.info("Iniciando mezcla con crossfade dinámico...")
        combined = AudioSegment.empty()

        for i, audio_file in enumerate(audio_files):
            audio = AudioSegment.from_wav(audio_file)
            duration_ms = len(audio)

            if self.dynamic:
                crossfade_ms = min(
                    self.max_ms,
                    max(self.min_ms, int(duration_ms * self.ratio))
                )
            else:
                crossfade_ms = 10  # fallback fijo

            if i == 0:
                combined = audio
            else:
                combined = combined.append(audio.fade_in(5), crossfade=crossfade_ms)
                combined += AudioSegment.silent(duration=self.silence_duration)

            logger.info(f"Agregado con crossfade ({crossfade_ms} ms): {audio_file}")

        combined.export(output_path, format="wav")
        logger.info(f"Audio final combinado exportado: {output_path}")