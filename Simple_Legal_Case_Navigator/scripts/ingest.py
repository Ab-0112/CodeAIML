import argparse
from pathlib import Path
from app.utils import normalize_text
from app.rag import SimpleRAG

parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True)
args = parser.parse_args()

rag = SimpleRAG()

files = Path(args.path).glob("**/*.txt")
for f in files:
    text = normalize_text(f.read_text(encoding="utf-8", errors="ignore"))
    rag.add([text], [f.stem])

print("Ingested files into memory.")
