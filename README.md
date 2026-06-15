\# LegalRAG-Optima



A self-optimizing Retrieval-Augmented Generation (RAG) pipeline for legal document search, built using vector retrieval and cross-encoder re-ranking to improve search precision.



\## Overview



LegalRAG-Optima is a two-stage retrieval system designed for legal document exploration. Traditional semantic retrieval can return similar but irrelevant chunks. This project improves retrieval quality by combining:



\* \*\*Bi-Encoder Vector Retrieval\*\* for fast broad candidate search

\* \*\*Cross-Encoder Re-ranking\*\* for high-precision relevance scoring



This architecture improves the quality of retrieved legal clauses and helps reduce noise in downstream retrieval systems.



\---



\## Features



\* Legal document ingestion pipeline

\* Sentence-aware chunking with overlap

\* Embedding generation using Sentence Transformers

\* Persistent vector storage with ChromaDB

\* Baseline vector retrieval API

\* Advanced re-ranked retrieval API

\* Evaluation using MRR@5 and NDCG@10

\* Fully containerized with Docker and Docker Compose

\* Production-ready API with health checks



\---



\## System Architecture



```text

Raw Legal Documents

&#x20;       ↓

Data Ingestion \& Chunking

&#x20;       ↓

Chunked JSONL File

&#x20;       ↓

Embedding Generation

&#x20;       ↓

Chroma Vector Store

&#x20;       ↓

FastAPI Search API

&#x20;    ↙         ↘

Baseline      Re-ranked

Retrieval     Retrieval

&#x20;               ↓

&#x20;       Cross-Encoder Ranking

```



\---



\## Tech Stack



\* Python

\* FastAPI

\* ChromaDB

\* Sentence Transformers

\* Hugging Face Models

\* Docker

\* Docker Compose

\* Requests

\* NLTK



\---



\## Models Used



\### Bi-Encoder (Retriever)



\*\*sentence-transformers/all-MiniLM-L6-v2\*\*



Used for:



\* Query embeddings

\* Chunk embeddings

\* Fast semantic similarity search



Why:



\* Lightweight

\* Fast inference

\* Strong semantic performance



\---



\### Cross-Encoder (Re-ranker)



\*\*cross-encoder/ms-marco-MiniLM-L-6-v2\*\*



Used for:



\* Query-document pair scoring

\* Final ranking refinement



Why:



\* Better precision

\* Strong relevance understanding

\* Effective for reranking tasks



\---



\## Project Structure



```text

LegalRAG-Optima/

│

├── api/

│   └── routes.py

│

├── core/

│   ├── retriever.py

│   └── reranker.py

│

├── scripts/

│   ├── ingest.py

│   ├── embed.py

│   ├── evaluate.py

│   └── download\_data.py

│

├── data/

│   ├── raw/

│   └── processed/

│

├── evaluation/

│   └── queries.json

│

├── results/

│   └── evaluation\_metrics.json

│

├── docs/

│   └── technical\_analysis.md

│

├── vectorstore/

├── app.py

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── .env.example

└── README.md

```



\---



\## Setup Instructions



\### Clone Repository



```bash

git clone https://github.com/shahid200620/LegalRAG-Optima.git

cd LegalRAG-Optima

```



\---



\### Create Virtual Environment



Windows:



```bash

python -m venv venv

venv\\Scripts\\activate

```



\---



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Data Pipeline



\### Step 1: Generate Legal Dataset



```bash

python scripts/download\_data.py

```



This creates:



```text

data/raw/

```



with legal contract files.



\---



\### Step 2: Chunk Documents



```bash

python scripts/ingest.py

```



Output:



```text

data/processed/chunks.jsonl

```



Chunk format:



```json

{

&#x20; "doc\_id": "contract\_1",

&#x20; "chunk\_id": "contract\_1-1",

&#x20; "text": "contract text"

}

```



\---



\### Step 3: Generate Embeddings



```bash

python scripts/embed.py

```



Output:



```text

vectorstore/

```



\---



\## Running the API



Start locally:



```bash

uvicorn app:app --reload

```



Server:



```text

http://127.0.0.1:8000

```



\---



\## API Endpoints



\### Health Check



```http

GET /health

```



Response:



```json

{

&#x20; "status": "ok"

}

```



\---



\### Baseline Retrieval



```http

GET /api/v1/retrieve/baseline?query=confidential information\&k=5

```



Description:

Returns top-k vector similarity results.



\---



\### Re-ranked Retrieval



```http

GET /api/v1/retrieve/reranked?query=confidential information\&k=5

```



Description:

Returns top-k results after cross-encoder reranking.



\---



\## Evaluation



Run API first:



```bash

uvicorn app:app --reload

```



Then:



```bash

python scripts/evaluate.py

```



Output:



```text

results/evaluation\_metrics.json

```



Format:



```json

{

&#x20; "baseline": {

&#x20;   "mrr\_at\_5": 0.0,

&#x20;   "ndcg\_at\_10": 0.0

&#x20; },

&#x20; "reranked": {

&#x20;   "mrr\_at\_5": 0.0,

&#x20;   "ndcg\_at\_10": 0.0

&#x20; }

}

```



\---



\## Docker Setup



Build and run:



```bash

docker-compose up --build

```



Run in background:



```bash

docker-compose up --build -d

```



Stop:



```bash

docker-compose down

```



\---



\## Evaluation Metrics



\### MRR@5



Measures how quickly the first relevant document appears.



Higher is better.



\---



\### NDCG@10



Measures ranking quality while rewarding relevant documents appearing earlier.



Higher is better.



\---



\## Technical Analysis



Detailed analysis available in:



```text

docs/technical\_analysis.md

```



Includes:



\* Chunking strategy

\* Model selection reasoning

\* Failure mode analysis



\---



\## Future Improvements



\* Real-world legal corpora integration

\* Hybrid BM25 + Vector retrieval

\* Metadata-aware filtering

\* LLM answer generation layer

\* Better query expansion

\* Domain-specific fine-tuned rerankers



\---



\## Author



\*\*Shahid Mohammed\*\*



GitHub:

https://github.com/shahid200620



\---



\## License



This project is for educational and research purposes.



