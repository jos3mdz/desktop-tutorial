from django.db import models

# Create your models here.
class modelNote(models.Model):
    Title=models.CharField(max_length=50)
    Note=models.CharField(max_length=500)
