from rest_framework import routers

from backend.api.views import WordViewSet, LessonViewSet, MessageViewSet

router = routers.DefaultRouter()

router.register(r'messages', MessageViewSet)
router.register(r'word', WordViewSet)
router.register(r'lesson', LessonViewSet)
