from django.db import models
from django.core.files import File


# all data saves in database. Each file has an id and path
class Uploaded_File(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.FileField(upload_to='')

    def __str__(self):
        return str(self.file)
