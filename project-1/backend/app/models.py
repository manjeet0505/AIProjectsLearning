from sqlalchemy import Column, Integer, String
from pgvector.sqlalchemy import Vector

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_name = Column(String, nullable=False)
    chunk_text = Column(String, nullable=False)
    embedding = Column(Vector(1536))