from gtts import gTTS
import os


class AudioBuilder():

    def __init__(self):
        audiobuilder = self

    # Searching data in file storage
    def search_file(self, filename):
        return(f"audiotext/audiofiles/{filename}.mp3")

    # Build audiofile from text
    def build_audio(self, content, language):

        # Define a file storage
        audio_storage = "audiotext/audiofiles"
        text = content

        # Change a file name for database path
        audio_file_name = text[0:20].replace(' ', '_')

        # Initialize gTTS lib and hand over text and voice language
        generated_file = gTTS(text, lang=language)

        # Save completed file in storage
        generated_file.save(f"{audio_storage}/{audio_file_name}.mp3")

        # Return file name only
        return self.search_file(audio_file_name)
