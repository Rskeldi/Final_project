from django.urls import path

from apps.category import views

urlpatterns = [
    path('', views.CategoryApiView.as_view()),
]
