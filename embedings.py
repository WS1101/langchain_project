from langchain_ollama import OllamaEmbeddings

# MODEL_NAME = "llama-3.1-8b-instant"
MODEL_NAME = "nomic-embed-text-v2-moe"
# EMBEDDINGS = ollama
_embeddings = OllamaEmbeddings(model = MODEL_NAME)
def get_embeddings():
    return _embeddings
