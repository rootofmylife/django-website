from django.db import models
from django.forms import ModelForm

# Create your models here.
class FileUpload(models.Model):
    file = models.FileField(upload_to="file/")

class UploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ('file',)