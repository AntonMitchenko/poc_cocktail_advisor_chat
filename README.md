# Cocktail Advisor

**Cocktail Advisor** is a chat-based application that helps users explore cocktail recipes, ask questions about cocktails, and receive personalized recommendations based on their preferences. It uses a Retrieval-Augmented Generation (RAG) approach with a Language Model (LLM) and a vector database to deliver accurate and engaging responses.

## Features

- **Ask Questions:** Users can ask questions about cocktails and ingredients.
- **Personalized Recommendations:** The app remembers user preferences and suggests cocktails tailored to their taste.
- **Cocktail Database:** Provides detailed information about a variety of cocktails from a Kaggle dataset.
- **RAG Implementation:** Combines LLM-generated responses with data from the vector database for accuracy.
- **User-Friendly Interface:** Simple CLI or web-based interface for smooth interaction.

---

## Tech Stack

- **Backend:** Python
- **LLM Integration:** OpenAI GPT (or equivalent)
- **Vector Database:** FAISS, Pinecone, or Weaviate
- **Framework:** FastAPI (for web-based implementation)
- **Frontend:** HTML/JavaScript (for web interface)

---

## Installation

### Prerequisites

- Python 3.8+
- API key for OpenAI (or other LLM provider)
- Kaggle account (to download the dataset)
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/AntonMitchenko/poc_cocktail_advisor_chat.git
   cd poc_cocktail_advisor_chat
   ```

2. Set up a virtual environment:
   ```bash
   conda create -n poc_cocktail_advisor_chat python=3.11
   conda activate poc_cocktail_advisor_chat
   pip install pip-tools
   python -m pip install --upgrade pip
   pip-compile --output-file requirements.txt requirements.in
    ``` 

3. Install dependencies:
   ```bash
   pip install --user -r requirements.txt
   ```

4. Download the dataset from Kaggle:
   - [Cocktails Dataset](https://www.kaggle.com/datasets/aadyasingh55/cocktails?resource=download).
   - Place the dataset file (`cocktails.csv`) in the `data/` folder.

5. Set up environment variables:
   Create a `.env` file in the project root with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   VECTOR_DB_PATH=./data/vector_db
   ```

---

## Usage

### Run the Application

#### CLI Interface

1. Start the CLI application:
   ```bash
   python app/main.py
   ```

2. Type your questions, such as:
   - "What cocktails can I make with vodka?"
   - "Suggest a cocktail with lime and tequila."

#### Web Interface (Optional)

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. Interact with the chatbot via the web UI.

---

## Project Structure

```
├── data/
│   ├── raw/                     # Raw datasets
│   ├── preprocessed/            # Preprocessed datasets
│   └── embeddings/              # Embedding files and FAISS index
├── app/
│   ├── main.py                  # Main application logic (CLI or Streamlit entry point)
│   ├── streamlit_app.py         # Streamlit web interface
│   ├── database.py              # Vector database operations
│   ├── model.py                 # LLM integration (e.g., OpenAI GPT or HuggingFace)
│   ├── query.py                 # Query vector database and retrieve results
│   └── rag.py                   # Retrieval-Augmented Generation logic
├── models/
│   ├── __init__.py              # Package initializer
│   ├── embedder.py              # Embedding generation logic
│   └── vector_store.py          # Vector database setup and maintenance
├── requirements.txt             # Project dependencies
├── .env                         # Environment variables (API keys, config)
├── README.md                    # Project documentation
└── .gitignore                   # Ignored files and folders

```
---

## Future Improvements

- Add multi-language support.
- Extend dataset with user-contributed recipes.
- Enable voice-based interaction.
- Optimize for mobile devices.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

If you have any questions or feedback, feel free to reach out:
- Email: anton.mitchenko2003@gmail.com
- GitHub: [@AntonMitchenko](https://github.com/AntonMitchenko/poc_cocktail_advisor_chat)

---

Happy mixing! 🍸

