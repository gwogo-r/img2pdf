from pathlib import Path

from PIL import Image

from img2pdf.errors import (
    EmptyInputError,
    ImageReadError,
    MissingFileError,
    UnsupportedFormatError,
)

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}


def _check_extension(path: Path) -> None:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFormatError(
            f"Неподдерживаемый формат: {path.name} "
            f"(допустимы: {', '.join(sorted(SUPPORTED_EXTENSIONS))})"
        )


def _load_rgb_image(path: Path) -> Image.Image:
    try:
        img = Image.open(path)
        img.load()
    except OSError as e:
        raise ImageReadError(f"Не удалось прочитать изображение: {path}") from e

    # PNG с прозрачностью приводим к RGB
    if img.mode != "RGB":
        img = img.convert("RGB")
    return img


def images_to_pdf(image_paths: list[Path], output_path: Path) -> None:
    if not image_paths:
        raise EmptyInputError("Список изображений пуст")

    images: list[Image.Image] = []
    for path in image_paths:
        if not path.exists():
            raise MissingFileError(f"Файл не найден: {path}")
        _check_extension(path)
        images.append(_load_rgb_image(path))

    first, *rest = images
    first.save(
        output_path,
        "PDF",
        save_all=True,
        append_images=rest,
    )

    for img in images:
        img.close()
