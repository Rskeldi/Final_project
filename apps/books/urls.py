from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListApiView.as_view()),
    path('<int:pk>/', views.BookDetailApiView.as_view()),

]
