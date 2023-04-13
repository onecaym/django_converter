from django.test import TestCase
from django.template.defaultfilters import slugify
from audiotext.audiobuilder import AudioBuilder

class AudiotextTestCase(TestCase):

    def test_audiotext_creates_mp3_file(self):
        content = "test audio"
        language = "en"
        expected_location = "audiotext/audiofiles/test_audio.mp3"

        audiobuilder = AudioBuilder()

        audiofile_path = audiobuilder.build_audio(content, language)
        self.assertEqual(expected_location, audiofile_path)