from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    reader = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True)
