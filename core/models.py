from django.db import models

# Create your models here.
SEX = (('female', 'Female'), ('male', 'Male'))

class Customer(models.Model):
    name = models.charField(max_length=255)
    sex = models.CharField(choices=SEX)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name