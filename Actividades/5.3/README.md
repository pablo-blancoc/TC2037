# Pasos para ejecutar resaltador léxico con hilos en windows

1. Instalar Python versión 3 en adelante
2. Asegurarse que se instaló correctamente usando el comando python --version
3. Asegurarse de tener pip con el comando: pip -h
4. Ejecutar el comando: pip install virtualenv
5. Descargar archivos de repo: lexico.py, main.py, requirements.txt y tabla.csv. Crear una carpeta y almacenarlos en dicha carpeta.
6. Cambiar el directorio de la consola al de la carpeta donde se encuentran los archivos descargados
7. Ejecutar el comando: virtualenv venv
8. Ejecutar el comando: pip install -r requirements.txt
9. Si se desea -> Modificar valores de variables dentro del archivo main.py:
	- N: número de hilos
	- PATH: path de la carpeta donde se va a analizar los archivos
10. Ejecutar el comando: python main.py
11. Verificar resultados en carpeta donde se corrió. En esta carpeta se generarán los archivos ```.html```.

# Pasos para ejecutar resaltador léxico con hilos en MaMacOS
1. Abrir la terminal y ejecutar el siguiente comando 
```
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/Actividades/5.3/install.sh --output install.sh && bash install.sh
```
2. Dentro de la terminal desplegara las siguientes instrucciones a seguir

*Brucelords ;)*
