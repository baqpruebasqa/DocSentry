import os
from PyPDF2 import PdfReader
from docx import Document
import pandas as pd

# Funciones de lectura según el tipo de archivo
def leer_pdf(ruta):
    try:
        reader = PdfReader(ruta)
        return " ".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        return ""

def leer_word(ruta):
    try:
        doc = Document(ruta)
        return " ".join([p.text for p in doc.paragraphs])
    except Exception as e:
        return ""

def leer_excel(ruta):
    try:
        df = pd.concat(pd.read_excel(ruta, sheet_name=None), ignore_index=True)
        return " ".join(df.astype(str).stack())
    except Exception as e:
        return ""

def leer_txt(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return ""

# Clasificación del archivo
def clasificar_archivo(archivo):
    etiquetas = {"público": 0.1, "privado": 0.5, "secreto": 0.9}
    extension = os.path.splitext(archivo)[1].lower()

    if extension == ".pdf":
        texto = leer_pdf(archivo)
    elif extension in [".docx", ".doc"]:
        texto = leer_word(archivo)
    elif extension in [".xlsx", ".xls"]:
        texto = leer_excel(archivo)
    elif extension == ".txt":
        texto = leer_txt(archivo)
    else:
        return "no soportado", 0

    puntaje = sum(etiquetas.get(token.lower(), 0) for token in texto.split())
    nivel = "secreto" if puntaje > 0.7 else "privado" if puntaje > 0.3 else "público"
    return nivel, puntaje
