from pydantic import BaseModel
from typing import List

class AskRequest(BaseModel):
    query: str
    k: int = 5

class Evidence(BaseModel):
    id: str
    text: str
    score: float

class AskResponse(BaseModel):
    answer: str
    evidences: List[Evidence]
