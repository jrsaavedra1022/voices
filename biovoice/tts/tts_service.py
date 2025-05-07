from tts.interfaces.tts_engine import ITTSEngine
from tts.engine.coqui_engine import CoquiEngine

class TTSService:
    def __init__(self):
        self.engine: ITTSEngine = CoquiEngine()

    def generate_audio(self, text: str, output_path: str):
        self.engine.synthesize(text, output_path)