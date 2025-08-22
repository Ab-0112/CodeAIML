import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class SimpleRAG:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatIP(self.dim)
        self.metas = []

    def add(self, texts, ids):
        embs = self.model.encode(texts, normalize_embeddings=True)
        self.index.add(embs.astype(np.float32))
        for tid, txt in zip(ids, texts):
            self.metas.append({"id": tid, "text": txt})

    def search(self, query: str, k: int = 5):
        q_emb = self.model.encode([query], normalize_embeddings=True).astype(np.float32)
        scores, idxs = self.index.search(q_emb, k)
        results = []
        for i, s in zip(idxs[0], scores[0]):
            if i == -1: continue
            m = self.metas[i]
            results.append({"id": m["id"], "text": m["text"], "score": float(s)})
        return results
