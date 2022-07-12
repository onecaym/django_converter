from django.shortcuts import render, redirect
from pdf2word_conv.pdf2word_converter import *
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Uploaded_File

# Create your views here.

def index(request):
	return render(request, 'pdf2word_conv/index.html')

def success(request):
	return render(request, 'pdf2word_conv/success.html')

def conv_to_word(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded_file = Uploaded_File(file=request.FILES['file'])
			uploaded_file.save()
			f = Uploaded_File.objects.get(file=f"{request.FILES['file'].name}")
			converter = Converter()
			converter.create_file(f.file.path, f)


			return redirect('success')
	else:
		form = UploadFileForm()

	# return render(request, 'pdf2word_conv/conv_to_word.html')
	return render(request, 'pdf2word_conv/conv_to_word.html', {'form': form})