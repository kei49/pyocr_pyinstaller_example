import sys
import os
# import tesseract_patch
import pyocr

def configure_tesseract():
    
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        pyocr.tesseract.TESSERACT_CMD = os.path.join(base_path, 'tesseract_files', 'tesseract')
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    tesseract_path = os.path.join(base_path, 'tesseract_files', 'tesseract')
    tessdata_path = os.path.join(base_path, 'data', 'tessdata')
    
    print(tessdata_path)
    
    os.environ["PATH"] += os.pathsep + tesseract_path
    os.environ["TESSDATA_PREFIX"] = tessdata_path
