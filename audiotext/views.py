from django.shortcuts import render
from .forms import VoiceTextForm
from audiotext.audiobuilder import *
from .models import Uploaded_File
from django.http import FileResponse


# Create audio file from text
def create_audio(request):
    if request.method != "POST":

        # Display blank registration form.
        form = VoiceTextForm()
    else:
        # Process completed form.
        form = VoiceTextForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            # Define text language
            language = form.cleaned_data['language']

            # Initialize audio builder class
            audiobuilder = AudioBuilder()

            # Call build audio method
            audio_file = audiobuilder.build_audio(text, language)
            response = FileResponse(
                open(f'{audio_file}', 'rb'), as_attachment=True)
            return response

    return render(request, 'audiotext/create_audio.html', {'form': form})
