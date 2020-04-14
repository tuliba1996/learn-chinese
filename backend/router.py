from rest_framework import routers

from backend.api.views import WordViewSet, LessonViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'messages', MessageViewSet)
router.register(r'word', WordViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'user', UserViewSet)
# router.register(r'token/refresh', TokenRefreshView)

