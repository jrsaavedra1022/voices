import spacy
from typing import List

# Cargar el modelo de spaCy para español una sola vez
nlp = spacy.load("es_core_news_sm")

def split_text_into_sentences(text: str) -> List[str]:
    """
    Divide un texto largo en frases cortas y coherentes usando NLP.
    """
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return sentences