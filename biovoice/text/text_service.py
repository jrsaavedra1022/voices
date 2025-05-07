from text.processors.punctuation_enhancer import PunctuationEnhancer
from text.processors.sentence_splitter import SentenceSplitter

class TextService:
    def __init__(self):
        self.punctuation = PunctuationEnhancer()
        self.splitter = SentenceSplitter()

    def enhance_paragraphs(self, paragraphs: list[str]) -> list[str]:
        return [self.punctuation.process(p) for p in paragraphs]

    def split_sentences(self, paragraph: str) -> list[str]:
        return self.splitter.process(paragraph)