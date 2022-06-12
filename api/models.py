from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    expiry=models.DateField()

    def __str__(self):
        return self.name