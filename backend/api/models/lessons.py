from django.db import models

from backend.api.models.book import Book


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name
