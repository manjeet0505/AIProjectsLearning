from app.services.rag_service import ask_question


question = "What is RAG?"

answer = ask_question(question)

print("\n--- ANSWER ---")
print(answer)