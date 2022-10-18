from email.policy import default
from django.db import models

class Pertsona(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Kotxe(models.Model):
    alokatua = models.BooleanField(default = False)
    hasieradata = models.CharField(max_length=255, default = "")
    bukaeradata = models.CharField(max_length=255, default = "")
    pertsona = models.ForeignKey(Pertsona,on_delete = models.CASCADE, null = True)
    