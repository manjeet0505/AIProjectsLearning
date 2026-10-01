from app.services.document_service import extract_text_from_pdf, chunk_text

text = extract_text_from_pdf("test.pdf")

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)