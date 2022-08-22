from django.shortcuts import render
from .forms import VoiceTextForm
from audiotext.audiobuilder import *
from .models import Uploaded_File
from django.http import FileResponse


def create(request):
	if request.method != "POST":
		form = VoiceTextForm()
	else:
		form = VoiceTextForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			language = form.cleaned_data['language']
			audiobuilder = AudioBuilder()
			audio_file = audiobuilder.buildaudio(text, language)
			print(audio_file)
			response = FileResponse(
				open(f'{audio_file}','rb'), as_attachment=True)
			return response

	return render(request, 'audiotext/create.html', {'form': form})