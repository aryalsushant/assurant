   # src/utils.py
import PyPDF2

def extract_claim_info(pdf_path):
       with open(pdf_path, 'rb') as file:
           reader = PyPDF2.PdfReader(file)
           text = ''
           for page in reader.pages:
               text += page.extract_text()
       return text