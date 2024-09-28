import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import docx
import PyPDF2
from bs4 import BeautifulSoup

class FileReader:
    def __init__(self, master):
        self.master = master
        self.master.title("URLValidator")

        self.btn_open = tk.Button(self.master, text="Abrir archivo", command=self.open_file)
        self.btn_open.pack(pady=20)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"),
                       ("Word files", "*.docx"),
                       ("PDF files", "*.pdf"),
                       ("Web files", "*.html;*.htm")])
        
        if file_path.endswith('.xlsx'):
            self.read_excel(file_path)
        elif file_path.endswith('.docx'):
            self.read_word(file_path)
        elif file_path.endswith('.pdf'):
            self.read_pdf(file_path)
        elif file_path.endswith('.html') or file_path.endswith('.htm'):
            self.read_web(file_path)
        else:
            messagebox.showerror("Error", "Formato de archivo no soportado.")

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
            messagebox.showerror("Error", f"No se pudo leer el archivo Excel: {e}")
            return []

    def read_word(self, file_path):
        try:
            doc = docx.Document(file_path)
            urls = [(i, para.text) for i, para in enumerate(doc.paragraphs) if para.text]
            return urls 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo Word: {e}")
            return []

    def read_pdf(self, file_path):
        try:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                urls = []
                # Contador para las líneas
                line_index = 0  
                for page_idx, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        for line in text.splitlines():
                            line_index += 1 
                            urls.append((line_index, line.strip()))
            return urls 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo PDF: {e}")
            return []

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
            messagebox.showerror("Error", f"No se pudo leer el archivo web: {e}")
            return []