import numpy as np
from utils.logger import setup_logger

logger = setup_logger(__name__)

class RMSCompressor:
    def __init__(self, threshold: float = 0.03, ratio: float = 2.0, window_size: int = 2048):
        self.threshold = threshold
        self.ratio = ratio
        self.window_size = window_size

    def compress(self, y: np.ndarray) -> np.ndarray:
        logger.info(f"Aplicando compresión RMS: threshold={self.threshold}, ratio={self.ratio}")
        compressed = np.copy(y)
        total_samples = len(y)

        for start in range(0, total_samples, self.window_size):
            end = min(start + self.window_size, total_samples)
            window = y[start:end]
            rms = np.sqrt(np.mean(window**2))
            if rms > self.threshold:
                gain = (self.threshold + (rms - self.threshold) / self.ratio) / rms
                compressed[start:end] *= gain

        return compressed