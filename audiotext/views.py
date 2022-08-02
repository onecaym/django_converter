from django.shortcuts import render
from .forms import UploadFileForm
from audiotext.audiobuilder import *
from .models import Uploaded_File
from django.http import FileResponse


def create(request):
	if request.method != "POST":
		form = UploadFileForm()
	else:
		print(request)
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded_file = Uploaded_File(file=form.cleaned_data['file'])
			language = form.cleaned_data['language']
			uploaded_file.save()
			clear_filename = Uploaded_File.objects.get(file=f"{request.FILES['file'].name.replace(' ','_')}")
			audiobuilder = AudioBuilder()
			file_path = clear_filename.file.path
			audio_file = audiobuilder.buildaudio(file_path, clear_filename, language)
			response = FileResponse(
				open(f'{audio_file}','rb'), as_attachment=True)
			return response


	return render(request, 'audiotext/create.html', {'form': form})