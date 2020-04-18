from django.db import models
from .lessons import Lesson


class WordInLesson(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    chinese = models.CharField(max_length=255)
    pinyin = models.CharField(max_length=255)
    vietnamese = models.CharField(max_length=255)

    def __str__(self):
        return self.pinyin


class CommonChinese(models.Model):
    id = models.AutoField(primary_key=True)
    chinese = models.CharField(max_length=255)
    pinyin = models.CharField(max_length=255)
    vietnamese = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.pinyin
