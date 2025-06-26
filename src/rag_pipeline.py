import faiss
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

faiss_index = None
article_texts = []

def build_faiss_index(articles):
    global faiss_index, article_texts

    if not articles:
        faiss_index = None
        article_texts = []
        return

    embeddings = np.array(embedding_model.embed_documents(articles), dtype=np.float32)
    faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
    faiss_index.add(embeddings)
    article_texts = articles

def retrieve_relevant_docs(query):
    if faiss_index is None or not article_texts:
        return ["No relevant information found."]
    
    query_embedding = np.array(embedding_model.embed_query(query), dtype=np.float32).reshape(1, -1)
    _, result_ids = faiss_index.search(query_embedding, k=1)
    return [article_texts[i] for i in result_ids[0] if i < len(article_texts)] or ["No relevant information found."]

