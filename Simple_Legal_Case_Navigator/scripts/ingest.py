import argparse
from pathlib import Path
from app.utils import normalize_text
from app.rag import SimpleRAG
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return normalize_text(text)

parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True)
args = parser.parse_args()

rag = SimpleRAG()

files = Path(args.path).glob("**/*")
for f in files:
    if f.suffix.lower() == ".txt":
        text = normalize_text(f.read_text(encoding="utf-8", errors="ignore"))
    elif f.suffix.lower() == ".pdf":
        text = extract_text_from_pdf(f)
    else:
        continue  # skip unsupported formats

    if text.strip():
        rag.add([text], [f.stem])
        print(f"Ingested {f.name}")

print("✅ All documents ingested.")
