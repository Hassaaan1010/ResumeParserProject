import re
from docx import Document
import PyPDF2

def extract_data_from_resume(resume_file):
    print("Resume extraction started.")
    # Function to handle both PDF and Word files
    if resume_file.name.endswith('.pdf'):
        return extract_data_from_pdf(resume_file)
    elif resume_file.name.endswith('.docx'):
        return extract_data_from_docx(resume_file)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are allowed.")

def extract_data_from_pdf(resume_file):
    reader = PyPDF2.PdfReader(resume_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Use regex to extract first name, email, and mobile number
    return extract_candidate_info(text)

def extract_data_from_docx(resume_file):
    doc = Document(resume_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    
    # Use regex to extract first name, email, and mobile number
    return extract_candidate_info(text)


def extract_candidate_info(text):
    # Use regex patterns to extract candidate information
    # Assuming the name is usually the first non-empty line in the document
    lines = text.splitlines()
    first_name = None
    for line in lines:
        if line.strip():  # Skip empty lines
            first_name = re.match(r"^\b[A-Z][a-zA-Z]+\b", line)
            if first_name:
                first_name = first_name.group(0)
                break
    
    email = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    mobile_number = re.search(r"\+?\d{1,2}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}", text)

    return {
        'first_name': first_name if first_name else '',
        'email': email.group(0) if email else '',
        'mobile_number': mobile_number.group(0) if mobile_number else ''
    }

