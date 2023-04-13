from django.test import TestCase
from audiotext.models import Uploaded_File
from audiotext.audiobuilder import AudioBuilder
from django.template.defaultfilters import slugify

class AudiotextTestCase(TestCase):
    
    def test_audio_file_creation(self):
        test_filepath = 'audiotext/audiofiles/this_is_test.mp3'
        audiobuilder = AudioBuilder()
        language = "en"
        text = 'this is test'

        builded_audio = audiobuilder.build_audio(text, language)

        self.assertEqual(test_filepath, builded_audio)