from llm_response import generate_response

queries = [
    "I feel really hopeless and anxious.",
    "What are the symptoms of pneumonia?",
    "I want to end my life."
]

for query in queries:
    response = generate_response(query)
    print(f"**Query:** {query}\n**Response:** {response}\n{'-'*50}")
