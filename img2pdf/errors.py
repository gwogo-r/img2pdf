class Img2PdfError(Exception):
    """Базовая ошибка конвертера."""


class MissingFileError(Img2PdfError):
    pass


class UnsupportedFormatError(Img2PdfError):
    pass


class EmptyInputError(Img2PdfError):
    pass


class ImageReadError(Img2PdfError):
    pass
