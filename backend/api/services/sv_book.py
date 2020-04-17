from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from backend.api.models import Book
from backend.api.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')
