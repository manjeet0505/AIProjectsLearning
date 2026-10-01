from sqlalchemy.orm import Session

from app.models import DocumentChunk


def save_document_chunk(
    db: Session,
    document_name: str,
    chunk_text: str,
    embedding: list[float]
):
    document_chunk = DocumentChunk(
        document_name=document_name,
        chunk_text=chunk_text,
        embedding=embedding
    )

    db.add(document_chunk)
    db.commit()
    db.refresh(document_chunk)

    return document_chunk


def search_similar_chunks(
    db: Session,
    query_embedding: list[float],
    limit: int = 3
):
    results = (
        db.query(DocumentChunk)
        .order_by(
            DocumentChunk.embedding.cosine_distance(query_embedding)
        )
        .limit(limit)
        .all()
    )

    return results