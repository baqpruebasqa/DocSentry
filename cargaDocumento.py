from PyPDF2 import PdfReader
from transformers import pipeline

# Cargar y extraer texto de un PDF
reader = PdfReader("comprobante.pdf")
texto = " ".join([page.extract_text() for page in reader.pages])

# Modelo de clasificación de texto
clasificador = pipeline("text-classification", model="bert-base-uncased")
resultado = clasificador(texto)
print(resultado)
