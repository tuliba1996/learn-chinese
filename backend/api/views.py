from rest_framework import viewsets, filters, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from backend.api.models import User
from backend.api.serializers.serializers import MessageSerializer, LessonSerializer, WordSerializer
from backend.api.models.messages import Message
from backend.api.models.lessons import Lesson
from backend.api.models.words import WordInLesson
from backend.api.serializers.user import UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def get_word(self, request, *args, **kwargs):
        lesson_id = kwargs.get('pk', None)
        if lesson_id:
            list_word = WordInLesson.objects.filter(lesson=lesson_id)
            serializer = WordSerializer(list_word, many=True)
        return Response(JSONRenderer().render(serializer.data))


class WordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = WordInLesson.objects.all()
    serializer_class = WordSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'chinese', 'pinyin', 'vietnamese')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

