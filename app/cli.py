from app.models.query import search_similar
from app.models.rag import generate_response_with_rag
from sentence_transformers import SentenceTransformer
import faiss
import pickle

def main():
    print("Welcome to the Cocktail Chatbot!")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    index = faiss.read_index("../models/cocktail_faiss_index")

    with open("../data/cocktail_embeddings.pkl", 'rb') as f:
        data = pickle.load(f)

    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        results = search_similar(query, model, index, data)
        response = generate_response_with_rag(query, results)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
