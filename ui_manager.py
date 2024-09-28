import tkinter as tk
from tkinter import messagebox, filedialog, PhotoImage, ttk
import os
from url_validator_app import URLValidatorApp

class UIManager:
    def __init__(self, master):
        self.master = master
        self.master.title("URLValidator")
        self.master.geometry("1200x600")
        self.master.iconphoto(False, PhotoImage(file="assets/images/logo-icon.png"))
        
        self.frame = tk.Frame(self.master, bg="#688BF0")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.image = PhotoImage(file="assets/images/logo.png")
        self.image_label = tk.Label(self.frame, image=self.image, bg="#688BF0", height=100)
        self.image_label.pack(fill=tk.X)

        # Etiqueta para mostrar el estado del automata
        self.status_label = tk.Label(self.frame, text="Esperando un archivo a analizar", fg="white", highlightthickness=0, bg="#688BF0", font="8")
        self.status_label.pack(pady=20)
        
        # Contenedor para los botones
        self.button_frame = tk.Frame(self.frame, bg="#688BF0")
        self.button_frame.pack(padx=40)
        
        # Botón para seleccionar archivo
        self.select_button = tk.Button(self.button_frame, text="Seleccionar archivo", command=self.open_file, cursor="hand2", bg="#8CC7F5", font=('Arial', 10, 'bold'), width=20)
        self.select_button.pack(side=tk.LEFT, padx=20, pady=20)

        # Botón para abrir el archivo de reporte
        self.report_button = tk.Button(self.button_frame, text="Abrir reporte", command=self.open_report, state=tk.DISABLED, cursor="X_cursor", bg="#8CC7F5", font=('Arial', 10, 'bold'), width=15)
        self.report_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        # Se configuran estilos de tabla
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading", background="lightblue", foreground="black", font=('Arial', 10, 'bold'))
        self.style.configure("Treeview", background="#8CC7F5", fieldbackground="#8CC7F5", foreground="black")
        # Crea tabla
        self.tree = ttk.Treeview(self.frame, columns=("URL", "Status"), show="headings", )
        self.tree.heading("URL", text="URL")
        self.tree.heading("Status", text="Estado")
        self.tree.column("URL", width=370) 
        self.tree.column("Status", width=30, anchor="center")
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
        self.report_button.config(state=tk.NORMAL, cursor="hand2")
        for index, url, status in results:
                tag = 'valid' if status == 'URL válida' else 'invalid'
                self.tree.insert("", "end", values=(url, status), tags=(tag,)) 
    
    def disableSettings(self):
        self.tree.delete(*self.tree.get_children())
        self.status_label.config(text="Esperando un archivo a analizar")
        self.report_button.config(state=tk.DISABLED, cursor="X_cursor")