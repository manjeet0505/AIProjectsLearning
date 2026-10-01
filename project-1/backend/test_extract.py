from app.services.document_service import extract_text_from_pdf

text = extract_text_from_pdf("test.pdf")

print(text)