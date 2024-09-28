# from url_validator_dfa import URLValidatorDFA

# validator = URLValidatorDFA()

# print("Validador de URLs")
# print("Ingrese una URL para validar. Escriba 'salir' para terminar.\n")

# while True:
#     user_input = input("Ingrese una URL: ").strip()

#     if user_input.lower() == 'salir':
#         print("Validación finalizada.")
#         break

#     is_valid = validator.is_valid_url(user_input)

#     # Muestra si la URL es válida o no
#     if is_valid:
#         print(f"URL válida: {user_input}")
#     else:
#         print(f"URL no válida: {user_input}")
        
        # main.py
import tkinter as tk
from file_reader import FileReaderApp

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de Tkinter
    app = FileReaderApp(root)  # Inicializar la clase FileReaderApp
    root.mainloop()  # Iniciar el bucle de la interfaz

