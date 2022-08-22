from gtts import gTTS
import os

class AudioBuilder():

	def __init__(self):
		audiobuilder = self

	def search_file(self, filename):
		return(f"audiotext/audiofiles/{filename}.mp3")

	def buildaudio(self, content, language):
		audio_folder = "audiotext/audiofiles"
		text = content.replace(' ','_')
		file_name = text[0:20]
		prepared_file = gTTS(text, lang=language)
		audio_file = prepared_file.save(f"{audio_folder}/{file_name}.mp3")
		
		return self.search_file(file_name)