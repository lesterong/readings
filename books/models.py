import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    read_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.title} ({self.author})"
