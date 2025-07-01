# Firmador Masivo de PDFs

Este script en Python permite **firmar masivamente archivos PDF** dentro de una estructura de carpetas por año y mes.

## 🧾 Descripción

El script recorre una estructura de carpetas con la siguiente jerarquía:
```bash
D:/firmar_masivo_anual/
├── 2020/
│ ├── enero/
│ │ ├── 1.pdf
│ │ ├── 2.pdf
│ │ └── ...
│ └── ...
├── 2021/
│ └── ...
├── imagen/
│ └── firma.png
```

> Se admiten los años **2020 a 2024** y meses en español en minúsculas: `enero`, `febrero`, ..., `diciembre`.

Cada archivo PDF será firmado en la **última hoja**, en la **parte izquierda, centrado verticalmente**, dejando un margen de `20 px` desde el borde izquierdo.

El archivo firmado se guarda en una subcarpeta `firmados/` con el nombre `nombre_original_firmado.pdf`.

---

## 📦 Requisitos

- Python 3.10+
- Librerías:
  ```bash
  pip install pymupdf pillow

# Para Pruebas

Estructura de carpetas para realizar pruebas
```bash
├── firmar_masivo_anual/
|   └── 2020/
│   |   └── enero/
│   |       └── 1.pdf  (puede ser un dummy de prueba)
|   └── imagen/
|   |   └── firma.png  (nombre y formato obligatorio de img)
