# img2pdf — конвертер изображений в PDF (JPG, PNG, WebP, BMP)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**img2pdf** — бесплатная CLI-утилита на Python: несколько картинок → один PDF с сохранением порядка страниц.  
Подходит, если вам нужен **jpg2pdf**, **png2pdf**, **webp2pdf**, **bmp2pdf**, **image2pdf** или **images2pdf** без онлайн-сервисов и регистрации.

- JPG / JPEG → PDF  
- PNG → PDF (включая прозрачность — конвертируется в RGB)  
- WebP → PDF  
- BMP → PDF  
- несколько файлов разных форматов в один документ  

Нужен **Python 3.10+**. Команды выполняйте из каталога проекта (`requirements.txt`, `img2pdf.py`).

## Установка

### Windows

```powershell
python -m pip install -r requirements.txt
```

Если `python` не находится:

```powershell
py -3 -m pip install -r requirements.txt
```

### Linux и macOS

```bash
python3 -m pip install -r requirements.txt
```

## Запуск

### Windows

```powershell
python img2pdf.py image1.jpg image2.png -o result.pdf
```

```powershell
py -3 img2pdf.py image1.jpg image2.png -o result.pdf
```

### Linux и macOS

```bash
python3 img2pdf.py image1.jpg image2.png -o result.pdf
```

Без `-o` файл сохраняется как `output.pdf`.

**Windows:**

```powershell
python img2pdf.py photo1.png photo2.jpg photo3.webp
```

**Linux и macOS:**

```bash
python3 img2pdf.py photo1.png photo2.jpg photo3.webp
```

## Примеры

Несколько изображений в один PDF (на Windows: `python3` → `python`):

```bash
python3 img2pdf.py scan1.jpg scan2.jpg scan3.png -o scans.pdf
```

Одно изображение:

```bash
python3 img2pdf.py cover.png -o cover.pdf
```

## Поддерживаемые форматы

| Формат | Расширения | Поисковые запросы |
|--------|------------|-------------------|
| JPEG | `.jpg`, `.jpeg` | jpg to pdf, jpeg to pdf, jpg2pdf |
| PNG | `.png` | png to pdf, png2pdf |
| WebP | `.webp` | webp to pdf, webp2pdf |
| BMP | `.bmp` | bmp to pdf, bmp2pdf |

## Для владельца репозитория (SEO на GitHub)

После создания репозитория **https://github.com/gwogo-r/img2pdf** укажите на странице **Settings** или в блоке **About**:

**Description (кратко):**

```text
Convert JPG, PNG, WebP, BMP to PDF — CLI, Python, merge multiple images into one PDF
```

**Topics** (теги — сильно влияют на поиск внутри GitHub):

```text
jpg2pdf
png2pdf
webp2pdf
bmp2pdf
image-to-pdf
images-to-pdf
pdf-converter
convert-images-to-pdf
python
pillow
cli
command-line
open-source
```

## Ключевые слова (для поиска)

`img2pdf` · `image to pdf` · `images to pdf` · `picture to pdf` · `photo to pdf` · `merge images to pdf` · `combine images pdf` · `batch image to pdf` · `конвертер картинок в pdf` · `изображения в pdf` · `склейка фото в pdf`

## English

**img2pdf** is a free, open-source **command-line image to PDF converter** (MIT License). Merge **JPG, PNG, WebP, and BMP** into a single PDF file—order of pages matches the order of input files. No upload to third-party websites; runs locally with Python 3.10+ and [Pillow](https://pypi.org/project/Pillow/).

**Use cases:** jpg2pdf · png2pdf · webp2pdf · bmp2pdf · image2pdf · images2pdf · merge images to pdf · batch convert photos to pdf · scan to pdf from image files.

**Install** (from the project directory):

```bash
python3 -m pip install -r requirements.txt
```

**Run:**

```bash
python3 img2pdf.py photo.jpg scan.png -o document.pdf
```

On Windows, use `python` instead of `python3`. Default output file: `output.pdf` if `-o` is omitted.

**License:** [MIT](LICENSE) — Copyright (c) 2026 [gwogo-r](https://github.com/gwogo-r).
