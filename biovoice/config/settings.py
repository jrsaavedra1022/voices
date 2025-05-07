import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.input_dir = os.getenv("INPUT_DIR")
        self.json_dir = os.getenv("JSON_DIR")
        self.audio_output_dir = os.getenv("AUDIO_OUTPUT_DIR")
        self.model_dir = os.getenv("MODEL_DIR")
        self.log_dir = os.getenv("LOG_DIR")
        self.voice = os.getenv("VOICE")
        self.silence_duration_ms = int(os.getenv("SILENCE_DURATION_MS", 200))
        self.max_silence_ms = int(os.getenv("MAX_SILENCE_MS", 400))
        self.min_silence_len_ms = int(os.getenv("MIN_SILENCE_LEN_MS", 400))
        self.silence_thresh_db = int(os.getenv("SILENCE_THRESH_DB", -40))
        self.silence_fade_ms = int(os.getenv("SILENCE_FADE_MS", 20))
        self.crossfade_dynamic = os.getenv("CROSSFADE_DYNAMIC", "true").lower() == "true"
        self.crossfade_min_ms = int(os.getenv("CROSSFADE_MIN_MS", 5))
        self.crossfade_max_ms = int(os.getenv("CROSSFADE_MAX_MS", 25))
        self.crossfade_ratio = float(os.getenv("CROSSFADE_RATIO", 0.02))
        self.rms_threshold = float(os.getenv("RMS_THRESHOLD", 0.03))
        self.rms_ratio = float(os.getenv("RMS_RATIO", 2.0))
        self.bandpass_low_freq = int(os.getenv("BANDPASS_LOW_FREQ", 85))
        self.bandpass_high_freq = int(os.getenv("BANDPASS_HIGH_FREQ", 8000))
        self.target_lufs = float(os.getenv("TARGET_LUFS", -14.0))

        self._validate_directories()

    def _validate_directories(self):
        # Crea las carpetas principales si no existen
        for path in [self.input_dir, self.json_dir, self.audio_output_dir, self.model_dir, self.log_dir]:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

settings = Settings()