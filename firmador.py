import os
import fitz  # PyMuPDF
from PIL import Image

# Ruta base donde están los años (ajústalo si lo mueves)
RUTA_BASE = os.path.join("D:\\", "firmar_masivo_anual")

# Ruta a la imagen de la firma (debe estar en D:/usuario/imagen/firma.png)
RUTA_FIRMA = os.path.join(RUTA_BASE, "imagen", "firma.png")

# Años que deseas procesar (2020 a 2024)
ANIOS = list(range(2020, 2025))

# Meses esperados en español en minúsculas
MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "setiembre", "octubre", "noviembre", "diciembre"
]

# Método para firmar un PDF con una imagen de firma
def firmar_pdf(ruta_pdf, ruta_firma, ruta_destino):
    doc = fitz.open(ruta_pdf)
    firma = Image.open(ruta_firma)

    firma_path_temp = "firma_temp.png"
    firma.save(firma_path_temp)

    # Obtener la última página
    ultima_pagina = doc[-1]
    rect = ultima_pagina.rect

    # Tamaño deseado de la firma
    ancho_firma = 100
    alto_firma = 50

    # Coordenadas: margen izquierdo de 20px y centrado vertical
    x = 20
    y = (rect.height - alto_firma) / 2  # mitad vertical

    # Insertar la imagen en la última página
    ultima_pagina.insert_image(
        fitz.Rect(x, y, x + ancho_firma, y + alto_firma),
        filename=firma_path_temp
    )

    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
    doc.save(ruta_destino)
    doc.close()
    os.remove(firma_path_temp)

# Método para procesar el directorio y firmar los PDFs
def procesar_directorio():
    for anio in ANIOS:
        for mes in MESES:
            carpeta_mes = os.path.join(RUTA_BASE, str(anio), mes)
            print(f"📁 Revisando carpeta: {carpeta_mes}")
            if not os.path.exists(carpeta_mes):
                print(f"❌ Carpeta no existe: {carpeta_mes}")
                continue  # Saltar si no existe

            archivos = os.listdir(carpeta_mes)
            print(f"🔍 Archivos encontrados: {archivos}")
            for archivo in archivos:
                if archivo.endswith(".pdf"):
                    nombre = archivo.replace(".pdf", "")
                    ruta_pdf = os.path.join(carpeta_mes, archivo)
                    ruta_salida = os.path.join(carpeta_mes, "firmados", f"{nombre}_firmado.pdf")
                    print(f"✅ Firmando: {ruta_pdf}")
                    firmar_pdf(ruta_pdf, RUTA_FIRMA, ruta_salida)

if __name__ == "__main__":
    procesar_directorio()
    print("✅ Proceso completado.")
    input("Presiona ENTER para salir...")
