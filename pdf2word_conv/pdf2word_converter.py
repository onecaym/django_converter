from pdf2docx import parse

class Converter():

	def __init__(self):
		converter = self

	def create_file(self, path, name):
		pdf_file_path = path
		pdf_filename = f"pdf2word_conv/converted_files/{name}.docx"

		parse(pdf_file_path, pdf_filename)

		return pdf_filename