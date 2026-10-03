from app.db import SessionLocal
from app.services.embedding_service import create_embedding
from app.services.vector_service import search_similar_chunks


query = "What is RAG?"

query_embedding = create_embedding(query)

db = SessionLocal()

try:
    results = search_similar_chunks(
        db=db,
        query_embedding=query_embedding,
        limit=3
    )

    for result in results:
        print("\n--- RETRIEVED CHUNK ---")
        print("ID:", result.id)
        print("Document:", result.document_name)
        print("Text:", result.chunk_text)

finally:
    db.close()