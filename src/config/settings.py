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
        self.silence_duration_ms = int(os.getenv("SILENCE_DURATION_MS", 500))

        self._validate_directories()

    def _validate_directories(self):
        # Crea las carpetas principales si no existen
        for path in [self.input_dir, self.json_dir, self.audio_output_dir, self.model_dir, self.log_dir]:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

settings = Settings()