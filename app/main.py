import streamlit as st
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from models import search_similar, generate_response_with_rag

# Load resources
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')


@st.cache_resource
def load_faiss_index():
    return faiss.read_index("./app/models/cocktail_faiss_index")


@st.cache_resource
def load_data():
    with open("./data/cocktail_embeddings.pkl", 'rb') as f:
        return pickle.load(f)


# Initialize resources
st.title("Cocktail Chatbot")
st.write("Ask anything about cocktails or get recommendations!")

model = load_model()
index = load_faiss_index()
data = load_data()

# Input query from the user
query = st.text_input("Your query:")

if query:
    # Search similar cocktails
    with st.spinner("Searching for relevant cocktails..."):
        results = search_similar(query, model, index, data)

    # Display search results
    st.subheader("Relevant Cocktails:")
    if results:
        for result in results:
            st.markdown(f"**{result['name']}**")
            st.markdown(f"Ingredients: {', '.join(result['ingredients'])}")
            st.markdown(f"Instructions: {result['instructions']}")
            st.markdown("---")
    else:
        st.write("No relevant cocktails found.")

    # Generate a response using RAG
    with st.spinner("Generating response..."):
        response = generate_response_with_rag(query, results)

    # Display the generated response
    st.subheader("Chatbot Response:")
    st.write(response)

