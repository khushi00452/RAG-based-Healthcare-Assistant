from transformers import AutoTokenizer, AutoModelForCausalLM
from routing import route_query
from mental_health import CRISIS_RESPONSE
from medical_retrieval import fetch_pubmed_articles
from rag_pipeline import build_faiss_index, retrieve_relevant_docs

# Load LLM
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

def generate_response(query: str) -> str:
    """Generate a response to the user's health query."""
    query_type = route_query(query)

    if query_type == "crisis":
        return CRISIS_RESPONSE

    relevant_articles = fetch_pubmed_articles(query)[:3]
    build_faiss_index(relevant_articles)
    retrieved_docs = retrieve_relevant_docs(query)

    context = "\n".join(retrieved_docs) if retrieved_docs else "No relevant medical information found."

    prompt = f"""You are a healthcare assistant. Provide accurate, compassionate medical information based on the context below.

User Query: {query}

Medical Context:
{context}

Response:"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
