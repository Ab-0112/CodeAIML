from pydantic import BaseModel
import os

class Settings(BaseModel):
    DATA_DIR: str = os.getenv("DATA_DIR", "./data")
    INDEX_DIR: str = os.getenv("INDEX_DIR", "./data/indexes")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

settings = Settings()
