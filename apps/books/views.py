from rest_framework.generics import (ListCreateAPIView, )

from apps.books.models import Book
from apps.books.serializers import BookAPISerializer


class BookApiView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAPISerializer
