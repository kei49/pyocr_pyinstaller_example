# pyocr_pyinstaller_example

## Purpose

To generate simple ocr executable app by pyinstaller with tesseract.

## Dependencies and language models

Tesseract library needs to be installed locally

Language models can be downloaded from [tesseract-ocr](https://github.com/tesseract-ocr). Place tessdata model inside `tesseract_files/tessdata` when you change model to build by pyinstaller.

## Build by pyinstaller

```
pyinstaller --onefile --add-data "tesseract_files/tesseract:./tesseract_files" --add-data "tesseract_files/tessdata:./tesseract_files/tessdata" python_ocr/main.py --name python_ocr_fast
```

## Run executable with example image

```
./dist/python_ocr_fast input/ocr_example_1.png
```

Results should be like this below

`@ kei49 Initial commit 36fca®5 4minutesago )1commit`

## Bundles (this aproach didn't work to build general executable without forcing users to install tesseract)

```
cp /usr/local/Cellar/tesseract/5.3.2/lib/libtesseract.5.dylib tesseract_files/
cp /usr/local/opt/leptonica/lib/liblept.5.dylib tesseract_files/
cp /usr/local/opt/libarchive/lib/libarchive.13.dylib tesseract_files/

install_name_tool -change /usr/local/Cellar/tesseract/5.3.2/lib/libtesseract.5.dylib @executable_path/tesseract_files/libtesseract.5.dylib ./tesseract_files/tesseract
install_name_tool -change /usr/local/opt/leptonica/lib/liblept.5.dylib @executable_path/tesseract_files/liblept.5.dylib ./tesseract_files/tesseract
install_name_tool -change /usr/local/opt/libarchive/lib/libarchive.13.dylib @executable_path/tesseract_files/libarchive.13.dylib ./tesseract_files/tesseract
```
