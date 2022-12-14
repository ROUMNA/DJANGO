from django.db import models

class user (models.Model) : 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class formation (models.Model):
    modul = models.CharField(max_length=20)
    prix = models.IntegerField()
