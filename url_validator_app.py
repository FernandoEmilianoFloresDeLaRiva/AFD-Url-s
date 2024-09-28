from file_reader import FileReader
from url_validator_dfa import URLValidatorDFA
import csv

class URLValidatorApp(FileReader):
    def __init__(self, master):
        super().__init__(master)
        self.validator = URLValidatorDFA() 

    def read_excel(self, file_path):
        content = super().read_excel(file_path)
        self.validate_urls(content)

    def read_word(self, file_path):
        content = super().read_word(file_path)
        self.validate_urls(content)

    def read_pdf(self, file_path):
        content = super().read_pdf(file_path)
        self.validate_urls(content)

    def read_web(self, file_path):
        content = super().read_web(file_path)
        self.validate_urls(content)

    def validate_urls(self, urls):
        results = []  
        for index, url in urls:
            if self.validator.is_valid_url(url):
                print(f"Fila {index}: URL válida: {url}")
                results.append([index, url, "válida"])
            else:
                print(f"Fila {index}: URL no válida: {url}")
                results.append([index, url, "no válida"])

        # Guarda en un archivo CSV
        with open("resultados_url.csv", mode="w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Encabezados
            writer.writerow(["Fila, columna", "URL", "Estado"]) 
            # Escribe resultados
            writer.writerows(results)  

        print("Resultados guardados en resultados_url.csv")
