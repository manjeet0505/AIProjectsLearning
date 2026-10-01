from app.db import SessionLocal
from app.services.document_service import extract_text_from_pdf, chunk_text
from app.services.embedding_service import create_embedding
from app.services.vector_service import save_document_chunk


text = extract_text_from_pdf("test.pdf")

chunks = chunk_text(text)

db = SessionLocal()

try:
    for chunk in chunks:
        embedding = create_embedding(chunk)

        saved_chunk = save_document_chunk(
            db=db,
            document_name="test.pdf",
            chunk_text=chunk,
            embedding=embedding
        )

        print(f"Saved chunk with ID: {saved_chunk.id}")

finally:
    db.close()