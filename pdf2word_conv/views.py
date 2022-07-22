from django.shortcuts import render
from pdf2word_conv.pdf2word_converter import *
from .forms import UploadFileForm
from .models import Uploaded_File
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'pdf2word_conv/index.html')


def success(request):
    return render(request, 'pdf2word_conv/success.html')


@login_required
def conv_to_word(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = Uploaded_File(file=request.FILES['file'])
            uploaded_file.save()
            f = Uploaded_File.objects.get(file=f"{request.FILES['file'].name}")
            converter = FileConverter()
            if converter.get_extention(f.file.path) != '.pdf':
                messages.info(request, "Your file must have .pdf extention")
            else:
                converted_file = converter.create_file(f.file.path, f)
                response = FileResponse(
                    open(
                        f'{converted_file}',
                        'rb'),
                    as_attachment=True)
                return response
    else:
        form = UploadFileForm()

    # return render(request, 'pdf2word_conv/conv_to_word.html')
    return render(request, 'pdf2word_conv/conv_to_word.html', {'form': form})
