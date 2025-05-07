from abc import ABC, abstractmethod
from typing import Union, List

class ITextProcessor(ABC):
    @abstractmethod
    def process(self, text: Union[str, List[str]]) -> Union[str, List[str]]:
        """Procesa un texto o lista de textos."""
        pass