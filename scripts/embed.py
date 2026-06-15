import os
import json
import chromadb
from sentence_transformers import SentenceTransformer

CHUNK_FILE = "data/processed/chunks.jsonl"
VECTOR_PATH = "vectorstore"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=VECTOR_PATH)

collection = client.get_or_create_collection(name="legal_chunks")


def load_chunks():
    items = []

    with open(CHUNK_FILE, "r", encoding="utf-8") as file:
        for line in file:
            items.append(json.loads(line))

    return items


def create_embeddings():
    data = load_chunks()

    for item in data:
        embedding = model.encode(item["text"]).tolist()

        collection.add(
            ids=[item["chunk_id"]],
            documents=[item["text"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "doc_id": item["doc_id"]
                }
            ]
        )

    print("Embeddings stored successfully")


if __name__ == "__main__":
    create_embeddings()