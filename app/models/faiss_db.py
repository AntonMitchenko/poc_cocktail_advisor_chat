import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load embeddings
embeddings_path = "../../data/cocktail_embeddings.pkl"
with open(embeddings_path, 'rb') as f:
    data = pickle.load(f)

embeddings = np.array(data['embeddings'])
ids = np.array(data['ids'])

# Initialize FAISS index
dimension = embeddings.shape[1]  # Embedding vector size
index = faiss.IndexFlatL2(dimension)  # L2 similarity (Euclidean distance)

# Add embeddings to the index
index.add(embeddings)
print(f"FAISS index populated with {index.ntotal} embeddings.")

# Save the index to disk for future use
faiss.write_index(index, "cocktail_faiss_index")
print("FAISS index saved to cocktail_faiss_index.")


'''
Function to query the FAISS index
'''


def search_similar_cocktails(query, top_k=5):

    model = SentenceTransformer('all-MiniLM-L6-v2')

    query_embedding = model.encode(query, convert_to_numpy=True).reshape(1, -1)

    # Perform the search
    distances, indices = index.search(query_embedding, top_k)

    # Retrieve the cocktail details
    results = [data['data'][i] for i in indices[0]]
    return results


# Example: Search for cocktails similar to a query
query = "Gin, Lemon Juice, Grenadine"
results = search_similar_cocktails(query)
for i, result in enumerate(results, 1):
    print(f"{i}. {result['name']} - Ingredients: {result['ingredients']}")