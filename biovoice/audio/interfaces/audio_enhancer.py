# audio/interfaces/audio_enhancer.py

from abc import ABC, abstractmethod

class IAudioEnhancer(ABC):
    @abstractmethod
    def enhance(self, input_path: str, output_path: str = None) -> None:
        """
        Aplica una serie de mejoras al archivo de audio.

        Args:
            input_path (str): Ruta del archivo de entrada.
            output_path (str, opcional): Ruta del archivo de salida. Si no se proporciona, se sobrescribe el original.
        """
        pass