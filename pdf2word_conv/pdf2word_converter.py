from pdf2docx import Converter
import os.path


class FileConverter():

    def __init__(self):
        converter = self

    def create_file(self, path, name):
        filepath = path
        pdf_file = Converter(filepath)
        new_file_name = str(name)[:-4]
        word_file_path = f"pdf2word_conv/converted_files/{new_file_name}.docx"
        try:
            pdf_file.convert(word_file_path, multi_processing=True, cpu_count=2)

            return word_file_path
            pdf_file.close()
        except Exception:
            return(False)

