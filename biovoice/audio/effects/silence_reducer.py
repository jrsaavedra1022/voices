from pydub import AudioSegment
from pydub.silence import detect_silence
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SilenceReducer:
    def __init__(self):
        self.max_silence_ms = settings.max_silence_ms
        self.min_silence_len = settings.min_silence_len_ms
        self.silence_thresh = settings.silence_thresh_db
        self.fade_duration = settings.silence_fade_ms

    def reduce(self, audio: AudioSegment) -> AudioSegment:
        logger.info("Reducción de silencios largos en progreso...")
        output = AudioSegment.empty()
        silence_ranges = detect_silence(
            audio,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_thresh
        )

        last_pos = 0
        for start, end in silence_ranges:
            chunk = audio[last_pos:start]
            output += chunk

            silence_len = min(self.max_silence_ms, end - start)
            silence_chunk = AudioSegment.silent(duration=silence_len)

            if silence_len > self.fade_duration:
                silence_chunk = silence_chunk.fade_in(self.fade_duration)

            output += silence_chunk
            last_pos = end

        tail = audio[last_pos:]
        if len(tail) > self.fade_duration:
            tail = tail.fade_in(self.fade_duration)

        output += tail
        logger.info("Silencios reducidos correctamente.")
        return output