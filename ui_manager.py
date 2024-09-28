import tkinter as tk
from tkinter import messagebox, filedialog, PhotoImage, ttk
import os
from url_validator_app import URLValidatorApp

class UIManager:
    def __init__(self, master):
        self.master = master
        self.master.title("URLValidator")
        self.master.geometry("650x600")
        
        self.master.iconphoto(False, PhotoImage(file="assets/images/logo-icon.png"))
        
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.image = PhotoImage(file="assets/images/logo.png")
        self.image_label = tk.Label(self.frame, image=self.image)
        self.image_label.pack(pady=5)

        # Botón para seleccionar archivo
        self.select_button = tk.Button(self.frame, text="Seleccionar archivo", command=self.open_file)
        self.select_button.pack(pady=5)

        # Etiqueta para mostrar el estado del automata
        self.status_label = tk.Label(self.frame, text="Esperando un archivo a analizar")
        self.status_label.pack(pady=5)

        # Botón para abrir el archivo de reporte
        self.report_button = tk.Button(self.frame, text="Abrir reporte", command=self.open_report, state=tk.DISABLED)
        self.report_button.pack(pady=5)
        
        # Crear tabla
        self.tree = ttk.Treeview(self.master, columns=("URL", "Status"), show="headings")
        self.tree.heading("URL", text="URL")
        self.tree.heading("Status", text="Estado")
        self.tree.tag_configure('valid', background='lightgreen')
        self.tree.tag_configure('invalid', background='lightcoral')
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.validator_app = URLValidatorApp()

    def open_file(self):
        # Seleccionar el archivo
        file_path = filedialog.askopenfilename(
            filetypes=[("Todos los archivos", "*.*"), ("Archivos Excel", "*.xlsx"), ("Archivos PDF", "*.pdf"),
                       ("Archivos Word", "*.docx"), ("Archivos Web", "*.html")])
        if file_path:
            try:
                if file_path.endswith(".xlsx"):
                    results = self.validator_app.read_excel(file_path)
                    self.enableSettings(file_path, results)
                elif file_path.endswith(".pdf"):
                    results = self.validator_app.read_pdf(file_path)
                    self.enableSettings(file_path, results)
                elif file_path.endswith(".docx"):
                    results =  self.validator_app.read_word(file_path)
                    self.enableSettings(file_path, results)
                elif file_path.endswith(".html"):
                    results = self.validator_app.read_web(file_path)
                    self.enableSettings(file_path, results)
                else:
                    self.disableSettings()
                    messagebox.showerror("Error", "Formato de archivo no soportado.")
    
            except Exception as e:
                self.disableSettings()
                messagebox.showerror("Error", str(e))
    
    def open_report(self):
        report_path = "resultados_url.csv"
        if os.path.exists(report_path):
            os.startfile(report_path)
        else:
            messagebox.showerror("Error", "No se ha encontrado el reporte.")
    
    def enableSettings(self, file_path, results):
        # Borra contenido de la tabla
        self.tree.delete(*self.tree.get_children())
        # Extrae solo el nombre del archivo
        file_name = os.path.basename(file_path)
        self.status_label.config(text=f"¡Analisis del archivo '{file_name}' completado!")
        self.report_button.config(state=tk.NORMAL)
        for index, url, status in results:
                tag = 'valid' if status == 'URL válida' else 'invalid'
                self.tree.insert("", "end", values=(url, status), tags=(tag,)) 
    
    def disableSettings(self):
        self.tree.delete(*self.tree.get_children())
        self.status_label.config(text="Esperando un archivo a analizar")
        self.report_button.config(state=tk.DISABLED)