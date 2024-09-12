from django.db import models

class Currrency(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    dayChange = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Allarm(models.Model):
    name = models.ForeignKey(Currrency,on_delete=models.CASCADE)
    price = models.CharField(max_length=1000)
    up_or_downe = models.CharField(max_length=100)

    def __str__(self):
        return self.name.name

    

