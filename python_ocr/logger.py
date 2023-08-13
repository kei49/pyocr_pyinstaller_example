import logging
import sys

def configure_logger():
    # logger = logging.getLogger('pyocr')
    # logger.setLevel(logging.ERROR)

    logger_file = 'pyocr_pyinstaller_example.txt'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=logger_file,
                        filemode='a')
    
def handle_error(error_message: str):
    logging.exception(error_message, exc_info=True)
    sys.stderr.write(f"Error - {error_message}\n")
    sys.exit(1)