
import os

def get_embeddings(texts: list[str]) -> list[list[float]]:
# minimal dummy embeddings (replace with real API calls)
return [[float(len(t)) for _ in range(1536)] for t in texts]
