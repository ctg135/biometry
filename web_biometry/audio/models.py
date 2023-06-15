from django.db import models
from web_biometry.settings import VOICE_FILES
import os

class Voice(models.Model):
    voice = models.FileField(upload_to=os.path.join(VOICE_FILES, '%y-%m-%d'))
# Create your models here.
