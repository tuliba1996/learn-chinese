from rest_framework import serializers

from backend.api.models.messages import Message
from backend.api.models.words import WordInLesson
from backend.api.models.lessons import Lesson


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordInLesson
        fields = '__all__'


