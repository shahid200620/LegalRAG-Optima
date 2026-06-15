import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="vectorstore")

collection = client.get_collection("legal_chunks")


def search_documents(query, k=10):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    output = []

    for i in range(len(results["ids"][0])):
        output.append({
            "chunk_id": results["ids"][0][i],
            "doc_id": results["metadatas"][0][i]["doc_id"],
            "text": results["documents"][0][i],
            "score": results["distances"][0][i]
        })

    return output