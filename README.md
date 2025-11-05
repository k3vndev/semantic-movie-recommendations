# 🎬 Semantic Movie Recommendations

A **semantic movie recommendation system** powered by ChromaDB.
Built to explore how vector databases can *understand* movie descriptions and give smarter suggestions — not just keyword matches.

> 💡 *Basically: it finds movies that “feel” like what you’re describing.*


## ⚙️ Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/k3vndev/semantic-movie-recommendations.git
   cd semantic-movie-recommendations
   ```

2. **Install dependencies** (using [UV](https://github.com/astral-sh/uv))

   ```bash
   uv sync
   ```

## 🧠 Build the Movie Database

You’ll need a `movies.csv` dataset first — check `src/create_db.py` for details on where to get it.
Once ready, run:

```bash
uv run src/create_db.py
```

> 🧹 Each run rebuilds the ChromaDB from scratch, so feel free to tweak stuff.

You can control how many movies to embed using the `ROWS_COUNT` variable in that file.
More rows = better results (but slower processing).

## 🎥 Get Movie Recommendations

Once your database’s ready, ask it what to watch:

```bash
uv run src/recommend.py
```

Then type something like:

```
I want a sci-fi movie about space exploration
```

And it will return **3 semantically similar movies** that match the *vibe* of your query.


## 🧩 Tech Stack

* **Python**
* **ChromaDB** (vector database)
* **UV** (modern dependency manager)
* **Pandas** (data handling)