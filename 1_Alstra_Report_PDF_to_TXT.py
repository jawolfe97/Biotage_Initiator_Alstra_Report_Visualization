import os
import PyPDF2

def extract_pdfs_to_txt():
    # Get the folder where the script is located
    folder = os.path.dirname(os.path.abspath(__file__))

    # Loop over all PDF files in the folder
    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder, filename)
            txt_path = os.path.join(folder, os.path.splitext(filename)[0] + ".txt")

            # Open the PDF
            with open(pdf_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)

                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    # Iterate over pages
                    for i, page in enumerate(reader.pages, start=1):
                        text = page.extract_text() or ""
                        txt_file.write("\n")
                        txt_file.write(f"Page {i}\n")
                        txt_file.write(text)
                        txt_file.write("\n")

            print(f"Extracted: {filename} -> {os.path.basename(txt_path)}")

if __name__ == "__main__":
    extract_pdfs_to_txt()
