import os
import pathlib


"""
# Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.

# Listar los ficheros de una carpeta con os
 - Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
- Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
- Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os. 
 """
 
 
 
 
ruta = "C:/Users/Propietario/Downloads"
listado = os.listdir(ruta)


# Imprimir los ficheros
# usando os.path.isfile 
#print(listado)
print("\n**********************************************************\n")
print("Listado de ficheros:")
print("\n**********************************************************\n")
for file in listado:
    if os.path.isfile(ruta + "/" + file):
        print(file)
print("\n**********************************************************\n")
print("Listado de directorios:")
print("\n**********************************************************\n")

# Imprimir los directorios
# usando os.path.isdir
for file in listado:
    if os.path.isdir(ruta + "/" + file):
        print(file)
        
print("\n**********************************************************\n")
print("Listado de ficheros y directorios:")
print("\n**********************************************************\n")
# usando scandir , es como un iterador

with os.scandir(ruta) as ficheros:
    for fichero in ficheros:
        print(fichero.name)
print("\n**********************************************************\n")


# Imprimir solo los pdf
print("\n**********************************************************\n")
print("Listado de ficheros pdf:")
print("\n**********************************************************\n")

with os.scandir(ruta) as ficheros:
    for fichero in ficheros:
        if fichero.name.endswith(".pdf"):
            print(fichero.name) 
 
 
# iterando con condiciones
print("\n**********************************************************\n")
print("Listado de ficheros zip:")
print("\n**********************************************************\n")
with os.scandir(ruta) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.zip')]
    
print (ficheros)


# Listar subdirectorios con pathlib
print("\n**********************************************************\n")
print("Listado subdirectorios de un directorio:")
print("\n**********************************************************\n")

directorio = pathlib.Path(ruta)
ficheros = [fichero.name for fichero in directorio.iterdir() if fichero.is_dir()]
print(directorio, ficheros)






