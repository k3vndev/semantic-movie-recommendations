from consts import C
import chromadb

N_RESULTS = 3

user_query = input("Enter your query: ")

# Connect to ChromaDB and get the movies collection
client = chromadb.PersistentClient(path=C.CHROMADB_PATH)
collection = client.get_collection(name="movies")

print(f"Searching for movies...")

results = collection.query(
    query_texts=[user_query],
    n_results=N_RESULTS,
)

print(f"Top movie recommendations based on your query:\n({user_query})\n\n")
for i, doc in enumerate(results["documents"][0]):
    print(f"{i + 1}. {doc}\n")
    ids = ([str(i)],)
