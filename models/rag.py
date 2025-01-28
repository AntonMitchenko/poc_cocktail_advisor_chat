import openai


def generate_response_with_rag(query, search_results):
    context = "Relevant cocktails:\n"
    for result in search_results:
        context += f"- {result['name']} (Ingredients: {', '.join(result['ingredients'])})\n"
    augmented_query = f"{context}\nUser query: {query}"

    # send query LLM
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_query,
        max_tokens=150
    )
    return response['choices'][0]['text']
