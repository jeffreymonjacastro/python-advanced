import PyPDF2
from gtts import gTTS
import os

def extraer_texto_desde_pdf(archivo_pdf):
    texto = ""
    with open(archivo_pdf, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        num_paginas = len(lector.pages)
        for pagina in range(num_paginas):
            texto += lector.pages[pagina].extract_text()
        print(texto)
    return texto

def generar_audio_desde_texto(texto, archivo_audio):
    tts = gTTS(text=texto, lang='es')  # Se puede cambiar 'es' al código del idioma deseado
    tts.save(archivo_audio)

if __name__ == "__main__":
    archivo_pdf = input("Introduce el nombre del archivo PDF: ")
    archivo_mp3 = input("Introduce el nombre del archivo MP3: ")
    texto_extraido = extraer_texto_desde_pdf(archivo_pdf)
    archivo_audio = archivo_mp3 if archivo_mp3.endswith(".mp3") else archivo_mp3 + ".mp3"
    generar_audio_desde_texto(texto_extraido, archivo_audio)
    print(f"Se ha generado un archivo de audio '{archivo_audio}' con el texto del PDF.")
