from openai import OpenAI

from app.db import SessionLocal
from app.services.embedding_service import create_embedding
from app.services.vector_service import search_similar_chunks


client = OpenAI()


def ask_question(question: str):
    query_embedding = create_embedding(question)

    db = SessionLocal()

    try:
        chunks = search_similar_chunks(
            db=db,
            query_embedding=query_embedding,
            limit=3
        )
    finally:
        db.close()

    context = "\n\n".join(
        chunk.chunk_text
        for chunk in chunks
    )

    prompt = f"""
Answer the user's question using the provided context.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context, say:
"I don't know based on the provided documents."
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text