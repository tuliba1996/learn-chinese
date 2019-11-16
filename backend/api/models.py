from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    chinese = models.CharField(max_length=255)
    pinyin = models.CharField(max_length=255)
    vietnamese = models.CharField(max_length=255)

    def __str__(self):
        return self.pinyin

