from django.contrib import admin

from apps.books.models import Book, Favorites, Ratings

admin.site.register(Book)
admin.site.register(Favorites)
admin.site.register(Ratings)