import os

# Define las palabras y sus respectivos números
palabras_a_cambiar = {
    'Stop sign': '0',
    'Fire hydrant': '1',
    'Person': '2',
    'Animal': '3',
    'Auto part': '4',
    'Human face': '5'
}

# Ruta del directorio que contiene los archivos TXT
directorio = os.path.normpath('C:/Users/andre/Desktop/Vision_Robot/Code/Dataset/labels/train')

def reemplazar_palabras_en_archivo(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()

    # Reemplaza las palabras según el diccionario
    for palabra, numero in palabras_a_cambiar.items():
        contenido = contenido.replace(palabra, numero)

    # Escribe el contenido modificado de vuelta al archivo
    with open(archivo, 'w') as f:
        f.write(contenido)

def procesar_archivos_en_directorio(directorio):
    
    for archivo in os.listdir(directorio):
        print(archivo)
        if archivo.endswith(".txt"):
            
            archivo_path = os.path.join(directorio, archivo)
            reemplazar_palabras_en_archivo(archivo_path)

# Procesa todos los archivos en el directorio especificado
procesar_archivos_en_directorio(directorio)
