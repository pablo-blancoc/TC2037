-Pasos para ejecutar Resaltador léxico con hilos en windows-
Instalar Python versión 3 en adelante
Asegurarse que se instaló correctamente usando el comando python --version
Asegurarse de tener pip con el comando: pip -h
Ejecutar el comando: pip install virtualenv
Descargar archivos de repo: lexico.py, main.py, requirements.txt y tabla.csv. Crear una carpeta y almacenarlos en dicha carpeta.
Cambiar el directorio de la consola al de la carpeta donde se encuentran los archivos descargados
Ejecutar el comando: virtualenv venv
Ejecutar el comando: pip install -r requirements.txt
Si se desea -> Modificar valores de variables dentro del archivo main.py:
Ejecutar el comando: python main.py
Verificar resultados en carpeta test