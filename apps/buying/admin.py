from django.contrib import admin

from apps.buying.models import Order, Ordered

admin.site.register(Order)
admin.site.register(Ordered)