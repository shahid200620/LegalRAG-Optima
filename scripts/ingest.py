import os
import json
import nltk
from nltk.tokenize import sent_tokenize

RAW_FOLDER = "data/raw"
OUTPUT_FILE = "data/processed/chunks.jsonl"

CHUNK_SIZE = 5
OVERLAP = 2


def make_chunks(text):
    sentences = sent_tokenize(text)

    chunks = []
    start = 0

    while start < len(sentences):
        end = start + CHUNK_SIZE
        piece = sentences[start:end]
        chunk_text = " ".join(piece)

        chunks.append(chunk_text)

        start += CHUNK_SIZE - OVERLAP

    return chunks


def process_files():
    os.makedirs("data/processed", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        for filename in os.listdir(RAW_FOLDER):
            if filename.endswith(".txt"):
                doc_id = filename.replace(".txt", "")

                file_path = os.path.join(RAW_FOLDER, filename)

                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()

                chunks = make_chunks(text)

                for i, chunk in enumerate(chunks):
                    record = {
                        "doc_id": doc_id,
                        "chunk_id": f"{doc_id}-{i+1}",
                        "text": chunk
                    }

                    output.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    process_files()
    print("Chunks created successfully")