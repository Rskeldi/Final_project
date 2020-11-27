from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()


def poster_upload_to(instance, filename):
    return 'posters/{0}/{1} - {2}'.format(
        instance.publisher.fullname, instance.title, filename
    )


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    poster = models.ImageField(default='media/default_song.jpg',
                               upload_to=poster_upload_to, blank=True)
    hype = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    opinion = models.IntegerField(null=True, blank=True, validators=[
                                             MaxValueValidator(5),
                                             MinValueValidator(1)])

    def __str__(self):
        return f'{self.title} - {self.author} ---> {self.publisher.fullname}'
