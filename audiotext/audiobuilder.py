from gtts import gTTS
import os

class AudioBuilder():

	def __init__(self):
		audiobuilder = self

	def search_file(self, filename):
		return(f"audiotext/audiofiles/{filename}.mp3")

	def buildaudio(self, path, name, language):
		audio_folder = "audiotext/audiofiles"
		file_path = path
		new_name = str(name)[:-4]
		content = open(file_path)
		text = content.read()
		prepared_file = gTTS(text, lang=language)
		audio_file = prepared_file.save(f"{audio_folder}/{new_name}.mp3")
		
		return self.search_file(new_name)