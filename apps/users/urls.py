from django.urls import path, include

from .views import UserActivationView, UserPasswordReset

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('activate/<str:uidb64>/<str:token>/',
         UserActivationView.as_view()),
    path('password_reset/<str:uidb64>/<str:token>/',
         UserPasswordReset.as_view()),
]
