from fastapi import APIRouter
from core.retriever import search_documents
from core.reranker import rerank_documents

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "LegalRAG API is running"
    }


@router.get("/api/v1/retrieve/baseline")
def baseline(query: str, k: int = 10):
    results = search_documents(query, k)

    return {
        "results": results
    }


@router.get("/api/v1/retrieve/reranked")
def reranked(query: str, k: int = 10):
    results = rerank_documents(query, k)

    return {
        "results": results
    }