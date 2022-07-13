from django.db import models
from django.core.files import File

# Create your models here.

class Uploaded_File(models.Model):
	id = models.IntegerField(primary_key=True);
	file = models.FileField(upload_to='')

	def __str__(self):
		return str(self.file)