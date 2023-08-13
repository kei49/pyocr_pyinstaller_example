import ctypes
import os
import sys

tesseract_path = os.path.join(sys._MEIPASS, "tesseract")
os.chmod(tesseract_path, 0o755)  

from pyocr.libtesseract import tesseract_raw

g_libtesseract = tesseract_raw.g_libtesseract

def set_image_patched(handle, image):
    assert(g_libtesseract)

    image = image.convert("RGB")
    image.load()
    # imgdata = image.tobytes("raw", "RGB")
    imgdata = ctypes.c_char_p(image.tobytes("raw", "RGB"))

    g_libtesseract.TessBaseAPISetImage(
        ctypes.c_void_p(handle),
        imgdata,
        ctypes.c_int(image.width),
        ctypes.c_int(image.height),
        ctypes.c_int(3),  # RGB = 3 * 8
        ctypes.c_int(image.width * 3)
    )

    dpi = image.info.get("dpi", [tesseract_raw.DPI_DEFAULT])[0]
    g_libtesseract.TessBaseAPISetSourceResolution(ctypes.c_void_p(handle), dpi)

tesseract_raw.set_image = set_image_patched
