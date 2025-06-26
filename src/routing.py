from mental_health import CRISIS_KEYWORDS, MENTAL_KEYWORDS

def route_query(query: str) -> str:
    """Routes queries to Crisis, Mental Health, or Medical RAG."""
    query_lower = query.lower()

    if any(keyword in query_lower for keyword in CRISIS_KEYWORDS):
        return "crisis"
    if any(keyword in query_lower for keyword in MENTAL_KEYWORDS):
        return "mental"
    return "medical"
