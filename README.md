# PDF to TXT Extractor

This repository contains a Python script that automatically extracts text from all PDF files in the same folder as the script. For each PDF, the script creates a `.txt` file with the same base name, including page numbers and extracted text content.

## Features

- Iterates through all PDF files in the script's directory  
- Extracts text from every page  
- Writes output into `.txt` files with the same name as the original PDF  
- Each page in the `.txt` file includes:
Page N
<text from page>

markdown
Copy code
- Supports multi-page PDFs  
- Works with both newer and older versions of **PyPDF2**

## Requirements

- Python **3.8+**  
- [PyPDF2](https://pypi.org/project/PyPDF2/)  

Install PyPDF2 with:

```bash
pip install PyPDF2
Usage
Clone or download this repository.

Place the script in the same folder as your PDFs.

Run the script:

bash
Copy code
python pdf_to_txt.py
The script will create a .txt file for each .pdf file in the same folder.

Example:

Copy code
report.pdf   →   report.txt
Notes
If a PDF contains only scanned images, no text will be extracted (OCR is not included).

To add OCR functionality, consider using pytesseract or ocrmypdf.

Acknowledgments
PyPDF2 for PDF parsing

ChatGPT (by OpenAI) for assistance in developing and refining this script
