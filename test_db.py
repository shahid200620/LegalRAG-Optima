import chromadb

client = chromadb.PersistentClient(path="vectorstore")

collection = client.get_collection("legal_chunks")

print(collection.count())