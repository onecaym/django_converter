from django import forms


class VoiceTextForm(forms.Form):
    text = forms.CharField()
    language_choices = (("en", "English"),("fr", "French"),("zh-CN", "Mandarin (China Mainland)"),)
    language = forms.ChoiceField(choices = language_choices)
