from rest_framework.generics import (ListCreateAPIView, )

from apps.category.models import Category
from apps.category.serializers import CategoryAPISerializer


class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAPISerializer
