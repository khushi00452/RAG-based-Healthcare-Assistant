from pymed import PubMed
from Bio import Entrez
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import requests


Entrez.email = "khushi00452@gmail.com"
pubmed = PubMed(tool="HealthAI", email="khushi00452@gmail.com")

def fetch_pubmed_articles(query, max_results=5):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        return []
    
    result_ids = response.json().get("esearchresult", {}).get("idlist", [])
    return [f"PubMed Article ID: {article_id}" for article_id in result_ids]


