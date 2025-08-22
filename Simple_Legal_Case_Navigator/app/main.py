from fastapi import FastAPI
from .models import AskRequest, AskResponse, Evidence
from .rag import SimpleRAG

app = FastAPI(title="Simple Legal Navigator")
rag = SimpleRAG()

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    results = rag.search(req.query, k=req.k)
    answer = "Based on retrieved documents, here are the top matches."
    return AskResponse(
        answer=answer,
        evidences=[Evidence(**r) for r in results]
    )
