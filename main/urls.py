from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('apps.users.urls')),
    path('api/v1/category/', include('apps.category.urls'))
]
