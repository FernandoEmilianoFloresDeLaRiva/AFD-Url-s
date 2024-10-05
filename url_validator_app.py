from file_reader import FileReader
from AFD import Automata
from validator_txt import ValidatorTxt
from leer_afd_txt import leer_automata_de_txt
import csv

class URLValidatorApp(FileReader):
    def __init__(self):
        super().__init__()
        self.data = leer_automata_de_txt('automata.txt')
        self.validatorData = ValidatorTxt(self.data) 
        if self.validatorData.validar_existencia_alfabeto():
            self.validator = Automata(self.data)
        else:
            raise Exception('Define bien el automata')

    def read_excel(self, file_path):
        try:
            content = super().read_excel(file_path)
            return self.validate_urls(content)
        except Exception as e:
            raise Exception(e)

    def read_word(self, file_path):
        try:
            content = super().read_word(file_path)
            return self.validate_urls(content)
        except Exception as e:
            raise Exception(e)
            
    def read_pdf(self, file_path):
        try:
            content = super().read_pdf(file_path)
            return self.validate_urls(content)
        except Exception as e:
            raise Exception(e)

    def read_web(self, file_path):
        try: 
            content = super().read_web(file_path)
            return self.validate_urls(content)
        except Exception as e:
            raise Exception(e)

    def validate_urls(self, urls):
        results = []  
        for index, url in urls:
            if self.validator.validar_cadena(url):
                print(f"Fila {index}: URL válida: {url}")
                results.append([index, url, "URL aceptada"])
            else:
                print(url)
                print(f"Fila {index}: URL no válida: {url}")
                results.append([index, url, "URL invalida"])
            self.validator.restaurar_automata()
        self.generate_csv(results)
        return results

    def generate_csv(self, results):
        # Guarda en un archivo CSV
        with open("resultados_url.csv", mode="w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Encabezados
            writer.writerow(["Fila, columna", "URL", "Estado"]) 
            # Escribe resultados
            writer.writerows(results)  
        print("Resultados guardados en resultados_url.csv")
