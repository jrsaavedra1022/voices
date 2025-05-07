import spacy
from text.interfaces.text_processor import ITextProcessor

class SentenceSplitter(ITextProcessor):
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def process(self, text: str) -> list[str]:
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents if sent.text.strip()]