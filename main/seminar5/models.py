from django.db import models


class Data(models.Model):
    Name = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)
