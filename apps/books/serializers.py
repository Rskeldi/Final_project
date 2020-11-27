from rest_framework import serializers

from apps.books.models import Book


class BookAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            '__all__'
        )