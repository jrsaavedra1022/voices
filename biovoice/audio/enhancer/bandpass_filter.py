import numpy as np
import scipy.signal
from utils.logger import setup_logger

logger = setup_logger(__name__)

class BandpassFilter:
    def __init__(self, low_freq: int = 85, high_freq: int = 8000):
        self.low_freq = low_freq
        self.high_freq = high_freq

    def apply(self, y: np.ndarray, sr: int) -> np.ndarray:
        nyquist = sr / 2
        low = max(20, self.low_freq)
        high = min(self.high_freq, nyquist - 100)

        if not 0 < low < high < nyquist:
            raise ValueError(f"Frecuencias mal configuradas: low={low}, high={high}, nyquist={nyquist}")

        sos = scipy.signal.butter(
            N=4,
            Wn=[low, high],
            btype='bandpass',
            fs=sr,
            output='sos'
        )
        logger.info(f"Aplicando filtro pasa banda: {low}Hz - {high}Hz")
        return scipy.signal.sosfilt(sos, y)