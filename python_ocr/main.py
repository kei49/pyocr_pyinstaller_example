import sys
import logging
from PIL import Image

# import tesseract_patch
import tesseract
tesseract.configure_tesseract()

from logger import configure_logger, handle_error
configure_logger()

import pyocr
import pyocr.builders

    
class PythonOCR:
    def run(self):
        if len(sys.argv) < 2:
            error_message = "Please provide a path to the image file as an argument."
            handle_error(error_message)

        file_path = sys.argv[1]
        results = self._process_image(file_path)
        print(results)
        
    def _process_image(self, image_path, lang="eng"):
        tool = self._setup_tool(lang)
        try:
            txt = tool.image_to_string(
                Image.open(image_path),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
        except Exception as e:
            error_message = f"Failed to process image for {image_path=} with {lang=}: {e}"
            handle_error(error_message)
        
        return txt
        
    def _setup_tool(self, lang):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            logging.error("No OCR tool found")
            sys.exit(1)
        tool = tools[0]
        logging.debug("Will use tool '%s'" % (tool.get_name()))

        langs = tool.get_available_languages()
        logging.debug("Available languages: %s" % ", ".join(langs))
        
        if lang not in langs:
            error_message = f"Language '{lang}' is not available"
            handle_error(error_message)
        
        return tool


if __name__ == "__main__":
    app = PythonOCR()
    app.run()