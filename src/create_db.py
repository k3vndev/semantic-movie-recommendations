import pandas as pd
import json
import chromadb
from consts import C
from tqdm import tqdm

"""
Reads the movies dataset, embeds the movie titles, and saves the embeddings to a CSV file.

Instructions to prepare the dataset:
1. Download and unzip the dataset from https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
2. Put movies_metadata.csv into the root folder
3. Rename it to movies.csv
"""

ROWS_COUNT = 200  # Number of rows to process. Max 45466

print("Reading movies dataset...")
df = pd.read_csv("movies.csv")

print("Extracting relevant columns...")
df = df[["title", "release_date", "overview", "genres"]]

# Limit to a certain number of rows for quicker processing
df = df.head(ROWS_COUNT)

# Prepare texts for embedding
print("Preparing texts for embedding...")
to_embed = []

for index, row in df.iterrows():
    title = row["title"]
    release_date = row["release_date"]
    overview = row["overview"]

    # Extract the genres from the JSON-like string
    raw_genres = row["genres"]
    try:
        genres_list = json.loads(raw_genres.replace("'", '"'))
        genres = [genre["name"] for genre in genres_list]
    except json.JSONDecodeError:
        genres = []

    text = f"Title: {title}\nRelease Date: {release_date}\nOverview: {overview}\nGenres: {', '.join(genres)}"
    to_embed.append(text)

print(f"Saving {len(to_embed)} movie entries to ChromaDB...")

# Create chromadb collection
client = chromadb.PersistentClient(path=C.CHROMADB_PATH)
collection_name = "movies"

# If the collection exists, delete it first
if collection_name in [c.name for c in client.list_collections()]:
    client.delete_collection(collection_name)

collection = client.create_collection(name=collection_name)

for i, text in enumerate(tqdm(to_embed, desc="Adding to ChromaDB")):
    collection.add(
        documents=[text],
        metadatas={"index": i},
        ids=[str(i)],
    )

print("Movie entries successfully saved to ChromaDB!")
