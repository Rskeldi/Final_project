from django.urls import path, include

from .views import UserActivationView, UserDetail, UserList, UserPasswordReset

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('<int:pk>/', UserDetail.as_view()),
    path('activate/<str:uidb64>/<str:token>/',
         UserActivationView.as_view()),
    path('qwerty/<str:uidb64>/<str:token>/', UserPasswordReset.as_view()),
]
# from djoser.urls.jwt