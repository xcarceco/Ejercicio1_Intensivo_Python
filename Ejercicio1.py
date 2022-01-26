#Ejercicio imprimir los ficheros de la carpeta descargas
import os

ruta= '/Users/xavi/Downloads/'

dirs= os.listdir(ruta)

for file in dirs:
    print(file)
