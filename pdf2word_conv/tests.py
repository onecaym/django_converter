# from django.test import TestCase
# from django.template.defaultfilters import slugify
# from pdf2word_conv.models import Uploaded_File
# from pdf2word_conv.pdf_converter import FileConverter


# class ConverterTestCase(TestCase):
	
#     def test_files_saves_correctly(self):
#         """Files are saving"""
#         uploaded_file = Uploaded_File.objects.create(file="test file name")

#         uploaded_file.file = "test-file-name"
#         uploaded_file.save()
#         self.assertEqual(uploaded_file.file, slugify(uploaded_file.file))

#     def correct_file_convertation(self):
#     	target_path = "test_files/test_file.pdf"
#     	target_name = "test_file.pdf"
#     	expected_location = "pdf2word_conv/converted_files/test_file.docx"

#     	converter = FileConverter()

#     	word_file_location = converter.create_file(target_path, target_name)
#     	self.assertEqual(expected_location, word_file_location)

#     def incorrect_file_exception(self):
#     	target_path = "test_files/test_file_with_pictures.pdf"
#     	target_name = "test_file_with_pictures.pdf"

#     	converter = FileConverter()

#     	result = converter.create_file(target_path, target_name)
#     	print("result")
#     	self.assertRaises(ExpectedException, afunction)


