print("funciona")

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