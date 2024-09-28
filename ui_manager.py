import tkinter as tk
from tkinter import messagebox, filedialog
import os
from url_validator_app import URLValidatorApp

class UIManager:
    def __init__(self, master):
        self.master = master
        self.master.title("URLValidator")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Botón para seleccionar archivo
        self.select_button = tk.Button(self.frame, text="Seleccionar archivo", command=self.open_file)
        self.select_button.pack(pady=5)

        # Etiqueta para mostrar el estado del automata
        self.status_label = tk.Label(self.frame, text="Esperando a que el autómata analice el archivo...")
        self.status_label.pack(pady=5)

        # Botón para abrir el archivo de reporte
        self.report_button = tk.Button(self.frame, text="Abrir reporte", command=self.open_report, state=tk.DISABLED)
        self.report_button.pack(pady=5)

        self.validator_app = URLValidatorApp()

    def open_file(self):
        
        # Seleccionar el archivo
        file_path = filedialog.askopenfilename(
            filetypes=[("Todos los archivos", "*.*"), ("Archivos Excel", "*.xlsx"), ("Archivos PDF", "*.pdf"),
                       ("Archivos Word", "*.docx"), ("Archivos Web", "*.html")])
        if file_path:
            try:
                if file_path.endswith(".xlsx"):
                    self.validator_app.read_excel(file_path)
                    self.status_label.config(text="Análisis completado.")
                elif file_path.endswith(".pdf"):
                    self.validator_app.read_pdf(file_path)
                    self.status_label.config(text="Análisis completado.")
                elif file_path.endswith(".docx"):
                    self.validator_app.read_word(file_path)
                    self.status_label.config(text="Análisis completado.")
                elif file_path.endswith(".html"):
                    self.validator_app.read_web(file_path)
                    self.status_label.config(text="Análisis completado.")
                else:
                    messagebox.showerror("Error", "Formato de archivo no soportado.")
                
                
                
                # Habilita el botón para abrir el reporte
                self.report_button.config(state=tk.NORMAL)

            except Exception as e:
                messagebox.showerror("Error", str(e))
    def open_report(self):
        report_path = "resultados_url.csv"
        if os.path.exists(report_path):
            os.startfile(report_path)
        else:
            messagebox.showerror("Error", "No se ha encontrado el reporte.")
    
    