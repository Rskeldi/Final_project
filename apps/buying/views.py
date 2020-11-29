from requests import Response
from rest_framework import generics, status, serializers

from apps.buying.models import Order, Ordered
from apps.books.models import Book
from .serializers import OrderCreateSerializer, OrderDetailSerializer


class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        elif self.request.method == 'GET':
            return OrderDetailSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.keys == 3:
            ordered = []
            if data.get('ordered'):
                for i in data.get('ordered'):
                    if len(i.keys()) == 2:
                        try:
                            book = i['book']
                        except:
                            raise serializers.ValidationError('Не правильно '
                                                              'указана книга')
                        try:
                            quantity = i['quantity']
                        except:
                            raise serializers.ValidationError('Не правильно '
                                                              'указано количество')
                        book = Book.objects.get(pk=book)
                        if book.quantity >= quantity:
                            book.quantity -= quantity
                            book.save()
                        else:
                            raise serializers.ValidationError(
                                "Нету такого количества товара"
                            )
                        obj = Ordered.objects.create(quantity=quantity, book=book)
                        ordered.append(obj.pk)
                    else:
                        raise serializers.ValidationError(
                            'Не правильно переданы данные')
                request.data['ordered'] = ordered
                return self.create(request, *args, **kwargs)
        else:
            raise serializers.ValidationError('Нужно передать три значения')
