from rest_framework import serializers

from backend.api.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'pk')

