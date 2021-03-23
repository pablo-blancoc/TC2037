def analyze(line: str):
    """Analiza cada una de las lineas del archivo

    Args:
        line (str): La línea a analizar
    """
    print(line)


def lexerAritmetico(archivo: str):
    """
    Función principal donde se lee el archivo y se mandan a llamar las demás funciones para realizar el procesamiento

    Args:
        archivo (str): Nombre del archivo que se tiene que leer
    """
    try:
        with open(archivo, 'r') as file:
            lines = file.readlines()
        for line in lines:
            analyze(line)
            
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
    
    
file = input("NOMBRE DEL ARCHIVO: ")
lexerAritmetico(archivo=file)