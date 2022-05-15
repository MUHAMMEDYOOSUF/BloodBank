from django.db import models

# Create your models here.

class donate(models.Model):
    name=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    age=models.IntegerField()
    phno=models.BigIntegerField()
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=250)
    sub=models.CharField(max_length=250)
    bloodgrp=models.CharField(max_length=250)

    def __str__(self):
        return self.name

