from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    daily_change = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Alarm(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    target_price = models.CharField(max_length=100)
    trend = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.currency.name}: {self.trend} at {self.target_price}"

