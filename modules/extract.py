import fitz  # pymupdf for PDFs
import docx

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"❌ Error extracting PDF text: {str(e)}")
    return text.strip()

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(docx_path)
        text = "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"❌ Error extracting DOCX text: {str(e)}")
    return text.strip()
