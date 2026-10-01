from app.services.document_service import extract_text_from_pdf, chunk_text
from app.services.embedding_service import create_embedding


text = extract_text_from_pdf("test.pdf")

chunks = chunk_text(text)

embedding = create_embedding(chunks[0])

print("Embedding created successfully!")
print("Number of dimensions:", len(embedding))
print("First 5 values:", embedding[:5])