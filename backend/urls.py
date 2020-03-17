"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from backend.api.auth.login import login_view
from .router import router


urlpatterns = [
    path('', never_cache(TemplateView.as_view(template_name='index.html'))),
    path('api/', include(router.urls)),
    path('login', login_view),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())
]


