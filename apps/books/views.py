from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView )

from apps.books.models import Book
from apps.books.serializers import BookAPISerializer


class BookListApiView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAPISerializer


class BookDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAPISerializer
