import nltk
import os
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from typing import List

def setup_nlp():
    nltk.download('punkt')
    nltk.download('stopwords')
    os.system("python -m spacy download en_core_web_sm")



nlp = spacy.load("en_core_web_sm")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text: str) -> str:
    tokens = word_tokenize(text.lower())
    return " ".join([stemmer.stem(w) for w in tokens if w.isalnum() and w not in stop_words])

def extract_keywords(text: str) -> List[str]:
    doc = nlp(text)
    return [token.text for token in doc if token.pos_ in ["NOUN", "ADJ"] and token.text.lower() not in stop_words]
