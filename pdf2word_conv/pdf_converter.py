from pdf2docx import Converter
import os.path


class FileConverter():

    def __init__(self):
        converter = self

    # This method converts .PDF to the .DOCX extension
    def create_file(self, path, name):
        file_path = path

        # Initialize converter library
        pdf_file = Converter(file_path)

        # Giving a file name
        new_file_name = str(name)[:-4]

        # Giving a filepath to the uploaded file
        new_file_path = f"pdf2word_conv/converted_files/{new_file_name}.docx"

        # Trying to convert file. It doesn't work if file have images
        try:
            pdf_file.convert(new_file_path, multi_processing=True, cpu_count=2)

            return new_file_path
            pdf_file.close()
        except Exception:
            return(False)
