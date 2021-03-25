import pandas as pd


def output(word: str, result: str):
    """Se escribe dentro de un archivo el resultado de cada una de las palabras

    Args:
        word (str): La palabra que se leyó
        result (str): El tipo de palabra que es
    """
    # Quita los espacios de las palabras
    word = word.strip()
    
    states = [
        "Estado inicial",
        "Variable",
        "Entero",
        "Flotante",
        "Error",
        "Error",
        "Real",
        "Resta",
        "Suma",
        "División",
        "Comentario",
        "Multiplicación",
        "Potencia",
        "Asignación",
        "Paréntesis que abre",
        "Paréntesis que cierra",
        "Error"
    ]
    
    with open("result.txt", "a+") as file:
        if word not in [" ", "\n", "\t", ""] and len(word) > 0:
            if result == -1:
                if len(word) > 40:
                    file.write(word.ljust(len(word)+10))
                else:
                    file.write(word.ljust(40))
                file.write("ERROR: Invalid character\n".ljust(24))    
            else:
                if len(word) > 40:
                    file.write(word.ljust(len(word)+10))
                else:
                    file.write(word.ljust(40))
                file.write(f"{states[result]}\n".ljust(len(states[result])))

def lexerAritmetico(archivo: str):
    """
    Función principal donde se lee el archivo y se mandan a llamar las demás funciones para realizar el procesamiento

    Args:
        archivo (str): Nombre del archivo que se tiene que leer
    """
    # Leer la tabla de transición
    try:
        tabla = pd.read_csv("tabla.csv")
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
        return
    
    # Crear un archivo de resultados limpio
    with open("result.txt", "w") as file:
        pass
        
    # Leer el archivo a analizar
    try:
        with open(archivo, 'r') as file:
            lines = file.readlines()
        for line in lines:
            analyze(line, tabla)
            
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
        return
    

file = input("NOMBRE DEL ARCHIVO: ")
lexerAritmetico(archivo=file)