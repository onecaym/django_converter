from django.test import TestCase
from django.template.defaultfilters import slugify
from pdf2word_conv.models import Uploaded_File

class ConverterTestCase(TestCase):

    def correct_file_convertation(self):
    	target_path = "test_files/test_file.pdf"
    	target_name = "test_file.pdf"
    	expected_location = "pdf2word_conv/converted_files/test_file.docx"

    	converter = FileConverter()

    	word_file_location = converter.create_file(target_path, target_name)
    	self.assertEqual(expected_location, word_file_location)