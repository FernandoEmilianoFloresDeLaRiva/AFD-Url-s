import pandas as pd
import docx
from bs4 import BeautifulSoup
import pdfplumber

class FileReader:
    def __init__(self):
        print("Clase FileReader cargada!")

    def read_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            urls = [] 
            urls = [(f"{row_index}, {col_index}", str(value).strip())
                    for row_index, row in df.iterrows()
                    for col_index, value in row.items() 
                    if isinstance(value, str) and value.strip()]

            # Devuelve una lista de (índice, URL)
            return urls  
        except Exception as e:
            raise Exception(f"No se pudo leer el archivo Excel: {e}")

    def read_word(self, file_path):
        try:
            doc = docx.Document(file_path)
            urls = [(i, para.text) for i, para in enumerate(doc.paragraphs) if para.text]
            return urls 
        except Exception as e:
            raise Exception(f"No se pudo leer el archivo Word: {e}")

    def read_pdf(self, file_path):
        try:
            with pdfplumber.open(file_path) as pdf:
                urls = []
                # Contador para las líneas
                line_index = 0  
                for page_idx, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        for line in text.splitlines():
                            line_index += 1 
                            urls.append((line_index, line.strip()))
            return urls 
        except Exception as e:
              raise Exception(f"No se pudo leer el archivo PDF: {e}")

    def read_web(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            lines = text.splitlines()
            urls = [(i, line.strip()) for i, line in enumerate(lines) if line.strip()]
            return urls
        except Exception as e:
            raise Exception(f"No se pudo leer el archivo web: {e}")