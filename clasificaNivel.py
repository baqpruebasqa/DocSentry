import os
from PyPDF2 import PdfReader
from docx import document
import pandas as pd

# Función para leer texto de archivos PDF
def leer_pdf(ruta):
    try:
        reader = PdfReader(ruta)
        texto = " ".join([page.extract_text() for page in reader.pages])
        return texto
    except Exception as e:
        print(f"Error leyendo PDF '{ruta}': {e}")
        return ""

# Función para leer texto de archivos Word
def leer_word(ruta):
    try:
        doc = Document(ruta)
        texto = " ".join([p.text for p in doc.paragraphs])
        return texto
    except Exception as e:
        print(f"Error leyendo Word '{ruta}': {e}")
        return ""

# Función para leer texto de archivos Excel
def leer_excel(ruta):
    try:
        # Leer todas las hojas y concatenar contenido
        df = pd.concat(pd.read_excel(ruta, sheet_name=None), ignore_index=True)
        texto = " ".join(df.astype(str).stack())  # Convertir todo a texto y concatenar
        return texto
    except Exception as e:
        print(f"Error leyendo Excel '{ruta}': {e}")
        return ""

# Función para leer texto de archivos de texto (.txt)
def leer_txt(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error leyendo TXT '{ruta}': {e}")
        return ""

# Función para procesar un archivo y clasificarlo
def procesar_archivo(ruta, etiquetas):
    extension = os.path.splitext(ruta)[1].lower()
    if extension == ".pdf":
        texto = leer_pdf(ruta)
    elif extension in [".docx", ".doc"]:
        texto = leer_word(ruta)
    elif extension in [".xlsx", ".xls"]:
        texto = leer_excel(ruta)
    elif extension == ".txt":
        texto = leer_txt(ruta)
    else:
        print(f"Tipo de archivo no soportado: {ruta}")
        return

    # Calcular puntaje y clasificación
    if texto:
        puntaje = sum(etiquetas.get(token.lower(), 0) for token in texto.split())
        nivel = (
            "secreto" if puntaje > 0.7
            else "privado" if puntaje > 0.3
            else "público"
        )
        print(f"Archivo: {ruta}\nClasificación: {nivel}, Puntaje: {puntaje}\n")
    else:
        print(f"No se pudo extraer texto del archivo: {ruta}")

# Función para procesar todos los archivos en un directorio
def procesar_directorio(directorio, etiquetas):
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            procesar_archivo(ruta_completa, etiquetas)

# Etiquetas y pesos para la clasificación
etiquetas = {
    "público": 0.1,
    "privado": 0.5,
    "secreto": 0.9
}

# Ruta del directorio a procesar
directorio = r"C:\Users\Oscar\Downloads"

# Procesar todos los archivos en el directorio
procesar_directorio(directorio, etiquetas)
