import spacy
from text.interfaces.text_processor import ITextProcessor
from utils.logger import setup_logger

logger = setup_logger(__name__)

class PunctuationEnhancer(ITextProcessor):
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def process(self, text: str) -> str:
        logger.info("Mejorando puntuación del párrafo...")
        doc = self.nlp(text)
        enhanced = ""

        for sent in doc.sents:
            cleaned = sent.text.strip()
            if not cleaned.endswith((".", "!", "?", ",")):
                last_token = sent[-1].pos_
                if last_token in {"NOUN", "VERB", "ADJ"}:
                    cleaned += ","
                else:
                    cleaned += "."
            enhanced += cleaned + " "

        return enhanced.strip()