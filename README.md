# Img2pdf

Конвертер изображений в один PDF-файл. Передаёте список картинок — получаете документ с тем же порядком страниц.

Нужен **Python 3.10** или новее. Команды ниже выполняйте из каталога проекта (где лежат `requirements.txt` и `img2pdf.py`).

## Установка

### Windows

```powershell
python -m pip install -r requirements.txt
```

Если `python` не находится, попробуйте:

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

Без `-o` результат сохраняется в `output.pdf`:

**Windows:**

```powershell
python img2pdf.py photo1.png photo2.jpg photo3.webp
```

**Linux и macOS:**

```bash
python3 img2pdf.py photo1.png photo2.jpg photo3.webp
```

## Примеры

Несколько файлов в один PDF (на Windows замените `python3` на `python`):

```bash
python3 img2pdf.py scan1.jpg scan2.jpg scan3.png -o scans.pdf
```

Одно изображение:

```bash
python3 img2pdf.py cover.png -o cover.pdf
```

## Поддерживаемые форматы

- JPG / JPEG
- PNG
- WebP
- BMP
