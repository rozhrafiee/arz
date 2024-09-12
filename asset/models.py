from django.db import models

class Currrency(models.Model):
    name = models.CharField(max_length=100)
    

