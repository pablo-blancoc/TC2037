#!/bin/bash
mkdir Brucelords
cd Brucelords
pip install virtualenv
virtualenv venv
source venv/bin/activate
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/DFA/requirements.txt > requirements.txt
pip3 install -r requirements.txt
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/DFA/tabla.csv > tabla.csv
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/DFA/automata.py > automata.py
curl https://raw.githubusercontent.com/pablo-blancoc/TC2037/master/DFA/README.txt > README.txt
clear
echo "============================================"
echo "============================================"
echo ""
echo "Listo!"
echo "IMPORTANTE:"
echo "* Se ha creado una nueva carpeta Brucelords con todos los archivos necesarios, entra a ella para ejecutar el programa con el comando: cd Brucelords"
echo "* Para correr el programa recuerda activar el ambiente virtual usando el comando: source venv/bin/activate"
echo "* Para correr el programa recuerda tener tu archivo para leer en esa carpeta"
echo "* Para correr el programa solo debes usar el comando: python automata.py"
echo "* Para desactivar el ambiente virtual usa el comando: deactivate"
echo ""
echo ""
echo "Todo listo! Diviertete!!"
echo "-- Brucelords"
echo ""
