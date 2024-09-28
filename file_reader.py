import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import docx
import PyPDF2
from bs4 import BeautifulSoup

class FileReaderApp:
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
            print("Contenido del archivo Excel:")
            print(df)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo Excel: {e}")

    def read_word(self, file_path):
        try:
            doc = docx.Document(file_path)
            content = '\n'.join([para.text for para in doc.paragraphs])
            print("Contenido del archivo Word:")
            print(content)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo Word: {e}")

    def read_pdf(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                content = ''
                for page in reader.pages:
                    content += page.extract_text()
            print("Contenido del archivo PDF:")
            print(content)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo PDF: {e}")

    def read_web(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            print("Contenido del archivo web:")
            print(soup.get_text())
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo web: {e}")


# Integrar la clase en tu programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = FileReaderApp(root)
    root.mainloop()
