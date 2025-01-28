import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle


def load_faiss_index(index_path):
    return faiss.read_index(index_path)


def search_similar(query, model, index, data, top_k=5):
    query_embedding = model.encode(query, convert_to_numpy=True).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    results = [data['data'][i] for i in indices[0]]
    return results
