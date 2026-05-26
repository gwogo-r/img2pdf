import argparse
from pathlib import Path

from img2pdf.converter import images_to_pdf
from img2pdf.errors import (
    EmptyInputError,
    ImageReadError,
    Img2PdfError,
    MissingFileError,
    UnsupportedFormatError,
)

DEFAULT_OUTPUT = Path("output.pdf")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Конвертер изображений в PDF",
    )
    parser.add_argument(
        "images",
        nargs="+",
        metavar="IMAGE",
        help="Пути к изображениям (порядок сохраняется в PDF)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Путь к выходному PDF (по умолчанию: output.pdf)",
    )
    return parser


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    return build_parser().parse_args(argv)


def run(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.images:
        print("Ошибка: не указано ни одного изображения")
        return 1

    image_paths = [Path(p) for p in args.images]
    output_path = Path(args.output) if args.output else DEFAULT_OUTPUT

    try:
        images_to_pdf(image_paths, output_path)
    except EmptyInputError:
        print("Ошибка: список файлов пуст")
        return 1
    except MissingFileError as e:
        print(f"Ошибка: {e}")
        return 1
    except UnsupportedFormatError as e:
        print(f"Ошибка: {e}")
        return 1
    except ImageReadError as e:
        print(f"Ошибка: {e}")
        return 1
    except Img2PdfError as e:
        print(f"Ошибка: {e}")
        return 1

    print(f"Готово: {output_path}")
    return 0
