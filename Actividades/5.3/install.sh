#!/bin/bash
COLOR='\033[0;33m'
NC='\033[0m'
mkdir Brucelords
cd Brucelords
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/Actividades/5.3/requirements.txt > requirements.txt
pip3 install -r requirements.txt
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/Actividades/5.3/lexico.py > lexico.py
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/Actividades/5.3/main.py > main.py
deactivate
clear
echo "============================================"
echo "============================================"
echo ""
echo "\t${COLOR}=== IMPORTANTE: ===${NC}"
echo "* Se ha creado una nueva carpeta Brucelords con todos los archivos necesarios, entra a ella para ejecutar el programa con el comando: cd Brucelords"
echo "* Para correr el programa recuerda activar el ambiente virtual usando el comando: source venv/bin/activate"
echo ""
echo "1. Entra al archivo main.py y modifica las variables:"
echo "\t\t${COLOR}PATH:\t\tEl directorio que va a buscar el programa para leer los archivos${NC}"
echo "\t\t${COLOR}N:\t\tEl número de consumidores que vas a tener (hilos) para analizar los archivos${NC}"
echo "\t\t${COLOR}BUFF_SIZE:\tEl tamaño del buffer de la cola (almacén) sobre el cuál se van a guardar los archivos para consumirlos${NC}"
echo "2. Para correr el programa solo debes usar el comando: python main.py"
echo "3. Para desactivar el ambiente virtual usa el comando: deactivate"
echo ""
echo "\t${COLOR}Los archivos de resultado se van a guardar en el mismo directorio con extensión html${NC}"
echo ""
echo ""
echo "Todo listo! Diviertete!!"
echo "-- Brucelords ;)"
echo ""
