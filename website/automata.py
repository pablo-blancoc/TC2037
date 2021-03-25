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
    
    with open("static/files/result.txt", "a+") as file:
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


def analyze(line: str, data: pd.DataFrame):
    """Analiza cada una de las lineas del archivo

    Args:
        line (str): La línea a analizar
    """
    # Inicializar las variables
    line = line.replace("\n", "").replace("\t", "")
    state = 0
    length = len(line)
    start = 0
    index = 0
    
    while index < length:
        letter = line[index]
        
        if letter == 'E':
            pass
        elif letter == ' ':
            letter = "SPACE"
        elif letter.isalpha() and letter.islower():
            letter = "alpha-minus"
        elif letter.isnumeric():
            letter = "number"
        elif letter.isalpha() and letter.isupper():
            letter = "alpha-mayus"
        else:
            pass
        
        # La letra no está dentro del vocabulario
        if letter not in data.columns or state == -1:
            if state == -1:
                if letter in '+-/^*=()' or letter == "SPACE":
                    output(line[start:index], state)
                    state = 0
                    start = index
                else:
                    index += 1
            else:
                if line[start:index] in "+-/^*=()" and line[start:index] != "":
                    output(line[start:index], state)
                    start += 1
                state = -1
                index += 1
            continue
            
        if state == 0:
            # Estado inicial
            state = data[letter][0]
            index += 1
            
            if state == 0:
                start += 1
                
        else:
            if state == data[letter][state]:
                index += 1
            else:
                if data[letter][state] == 0:
                    output(line[start:index], state)
                    start = index
                    index -= 1
                state = data[letter][state]
                index += 1
                
    output(line[start:index], state)
    
        
def lexerAritmetico():
    """
    Función principal donde se lee el archivo y se mandan a llamar las demás funciones para realizar el procesamiento

    Args:
        archivo (str): Nombre del archivo que se tiene que leer
    """
    # Leer la tabla de transición
    try:
        tabla = pd.read_csv("automata/tabla.csv")
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
        return
    
    # Crear un archivo de resultados limpio
    with open("static/files/result.txt", "w") as file:
        pass
        
    # Leer el archivo a analizar
    try:
        with open("static/files/archivo.txt", 'r') as file:
            lines = file.readlines()
        for line in lines:
            analyze(line, tabla)
            
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
        return
