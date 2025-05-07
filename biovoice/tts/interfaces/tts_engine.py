from abc import ABC, abstractmethod

class ITTSEngine(ABC):
    @abstractmethod
    def synthesize(self, text: str, output_path: str):
        """Genera un archivo de audio a partir de texto."""
        pass