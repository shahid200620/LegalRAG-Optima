from sentence_transformers import CrossEncoder
from core.retriever import search_documents

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(query, k=10):
    candidates = search_documents(query, k * 5)

    pairs = []

    for item in candidates:
        pairs.append((query, item["text"]))

    scores = model.predict(pairs)

    for i in range(len(candidates)):
        candidates[i]["score"] = float(scores[i])

    ranked = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked[:k]