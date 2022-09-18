from django.shortcuts import render
from pdf2word_conv.pdf_converter import *
from .forms import UploadFileForm
from .models import Uploaded_File
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'pdf2word_conv/index.html')

# Only logged in user can use this application


@login_required
# This method takes a .PDF file from user input, saves it and converts to
# the .DOCX file
def pdf_converter(request):

    # Check type of request
    if request.method != 'POST':
        form = UploadFileForm()
    else:
        form = UploadFileForm(request.POST, request.FILES)

        # Check form valid
        if form.is_valid():
            uploaded_file = Uploaded_File(file=request.FILES['file'])
            uploaded_file.save()

            # Changing a file name for database
            changed_file_name = Uploaded_File.objects.get(
                file=f"{request.FILES['file'].name.replace(' ','_')}")

            # Initialize FileConverter class to pass the .PDF file
            converter = FileConverter()
            converted_file = converter.create_file(
                changed_file_name.file.path, changed_file_name)

            # Check file readiness
            # If file wasn't generated, raise an error
            # This application work with files without images inside .PDF files
            # only
            if converted_file:
                response = FileResponse(
                    open(
                        f'{converted_file}',
                        'rb'),
                    as_attachment=True)
                return response
            else:
                messages.info(request, ".pdf files without images only!")

    return render(request, 'pdf2word_conv/pdf_converter.html', {'form': form})
