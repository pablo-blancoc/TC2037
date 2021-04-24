import pandas as pd


def output(word: str, result: str):
    """Se escribe dentro de un archivo el resultado de cada una de las palabras

    Args:
        word (str): La palabra que se leyó
        result (str): El tipo de palabra que es
    """
    # Quita los espacios de las palabras
    word = word.strip()
    print("result: "+str(result))
    print("word:"+str(word))
    states = [
        "Estado inicial",
        "Identificador",
        "Numero",
        "Numero",
        "Error",
        "Error",
        "Numero",
        "Operador",
        "Operador",
        "Operador",
        "Comentario",
        "Operador",
        "Operador",
        "Operador",
        "Especiales",
        "Especiales",
        "Error",
        "Simbolo",
        "Logico",
        "BR"
    ]
    
    colores = {
        "Numero": "#ffe119",
        "Logico":"#4363d8",
        "Simbolo": "#469990",
        "Operador": "#911eb4",
        "Identificador" :"#3cb44b",
        "Especiales": "#9A6324",
        "Comentario": "#808000",
        "Palabras Reservadas": "#f032e6",
        "Error": "#e6194B",
        "BR": "<br>"
        }
    
    
    with open("result.html", "a+") as file:
        if word not in ["\t ", ""] and len(word) > 0:
            #print(word)
            if result <= 0:
                file.write("<span style=color:#e6194B;>"+ word + "</span>")
            elif result == 19:
                file.write("<br>")
                
            else:
                if word == "define"  :
                    file.write("<span style=color:#e6194B;>"+ word + "</span>")
                else:
                    file.write("<span style=color:"+colores[states[result]]+";>"+ word + "</span>")
        
        
      

def analyze(line: str, data: pd.DataFrame):
    """Analiza cada una de las lineas del archivo

    Args:
        line (str): La línea a analizar
    """
    # Inicializar las variables
    
    line = line.replace("\n", "?").replace("\t", "")
   #line= line + ("\n")
   # line = line.replace("\n", "")
   # print(line)
    
    
    #print(line)
    state = 0
    length = len(line)
    start = 0
    index = 0
    
    
    while index < length :
        letter = line[index]
        #print(letter)
        
        if letter == 'E':
            pass
        elif letter == 't':
            pass
        elif letter == 'f':
            pass
        elif letter == "?":
            letter = "?"
        elif letter == ' ':
            letter = "SPACE"
            pass
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
                if letter in "+-/^*=();'" or letter == "SPACE"  :
                    output(line[start:index], state)
                    state = 0
                    start = index
                else:
                    index += 1
            else:
                if line[start:index] in "+-/^*=();'" and line[start:index] != "" :
                    output(line[start:index], state)
                    start += 1
                state = -1
                index += 1
            #print("state -1:"+str(state))
            continue
            
        if state == 0:
            # Estado inicial
           
            state = data[letter][0]
            index += 1
            
            if state == 0:
                start += 1
                
            #print("state o:"+str(state))     
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
                #print("state r:"+str(state))
    
                
    #print(state)
    output(line[start:index], state)
    
        
def lexerAritmetico(archivo: str):
    """
    Función principal donde se lee el archivo y se mandan a llamar las demás funciones para realizar el procesamiento

    Args:
        archivo (str): Nombre del archivo que se tiene que leer
    """
    # Leer la tabla de transición
    try:
        tabla = pd.read_csv("tabla5.csv")
    except FileNotFoundError:
        print(f'ERROR: El archivo "{archivo}" no se ha encontrado.')
        return
    
    # Crear un archivo de resultados limpio
    with open("result.html", "w") as file:
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
    

# file = input("NOMBRE DEL ARCHIVO: ")
lexerAritmetico(archivo="test.scm")