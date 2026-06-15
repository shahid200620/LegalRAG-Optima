import json
import math
import requests

BASE_URL = "http://127.0.0.1:8000"


def reciprocal_rank(results, relevant_docs):
    for index, item in enumerate(results[:5]):
        if item["doc_id"] in relevant_docs:
            return 1 / (index + 1)
    return 0


def dcg(results, relevant_docs):
    score = 0

    for index, item in enumerate(results[:10]):
        if item["doc_id"] in relevant_docs:
            score += 1 / math.log2(index + 2)

    return score


def ndcg(results, relevant_docs):
    actual = dcg(results, relevant_docs)

    ideal_list = [{"doc_id": doc} for doc in relevant_docs[:10]]
    ideal = dcg(ideal_list, relevant_docs)

    if ideal == 0:
        return 0

    return actual / ideal


def fetch_results(endpoint, query):
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        params={"query": query, "k": 10}
    )

    return response.json()["results"]


def evaluate():
    with open("evaluation/queries.json", "r", encoding="utf-8") as file:
        queries = json.load(file)

    baseline_mrr = []
    baseline_ndcg = []

    reranked_mrr = []
    reranked_ndcg = []

    for item in queries:
        query = item["query_text"]
        relevant_docs = item["relevant_docs"]

        baseline_results = fetch_results(
            "/api/v1/retrieve/baseline",
            query
        )

        reranked_results = fetch_results(
            "/api/v1/retrieve/reranked",
            query
        )

        baseline_mrr.append(
            reciprocal_rank(baseline_results, relevant_docs)
        )

        baseline_ndcg.append(
            ndcg(baseline_results, relevant_docs)
        )

        reranked_mrr.append(
            reciprocal_rank(reranked_results, relevant_docs)
        )

        reranked_ndcg.append(
            ndcg(reranked_results, relevant_docs)
        )

    final_results = {
        "baseline": {
            "mrr_at_5": sum(baseline_mrr) / len(baseline_mrr),
            "ndcg_at_10": sum(baseline_ndcg) / len(baseline_ndcg)
        },
        "reranked": {
            "mrr_at_5": sum(reranked_mrr) / len(reranked_mrr),
            "ndcg_at_10": sum(reranked_ndcg) / len(reranked_ndcg)
        }
    }

    with open("results/evaluation_metrics.json", "w", encoding="utf-8") as file:
        json.dump(final_results, file, indent=4)

    print("Evaluation completed")


if __name__ == "__main__":
    evaluate()