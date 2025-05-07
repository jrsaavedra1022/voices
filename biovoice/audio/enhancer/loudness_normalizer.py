import soundfile as sf
import pyloudnorm as pyln
from utils.logger import setup_logger

logger = setup_logger(__name__)

class LoudnessNormalizer:
    def __init__(self, target_lufs: float = -14.0):
        self.target_lufs = target_lufs

    def normalize(self, file_path: str):
        logger.info(f"Normalizando loudness a {self.target_lufs} LUFS: {file_path}")
        data, rate = sf.read(file_path)

        meter = pyln.Meter(rate)
        loudness = meter.integrated_loudness(data)

        if abs(self.target_lufs - loudness) > 0.1:
            normalized = pyln.normalize.loudness(data, loudness, self.target_lufs)
            sf.write(file_path, normalized, rate)
            logger.info(f"Loudness ajustado: {loudness:.2f} → {self.target_lufs:.2f}")
        else:
            logger.info("Loudness dentro del rango aceptable, no se aplicó normalización.")