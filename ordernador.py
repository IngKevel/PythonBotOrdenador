import os
import shutil

ruta_descargas = "C:\\Users\\Administrador\\Downloads\\"
ext_documentos = ['.docx', '.txt', '.doc', '.pdf', '.pptx']
ext_imagenes = ['.png', '.jpg', '.jpeg', '.gif']
ext_video = ['.mov', '.mp4']
ext_musica = ['.ogg']
ext_sfk = [".sfk"]

def ordenar(archivo, ext):
    print(archivo, ext)
    for i in ext_documentos:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Documentos')
    for i in ext_imagenes:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Imagenes')
    for i in ext_video:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Videos')
    for i in ext_musica:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Musica')

def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(archivo, ext)

main()