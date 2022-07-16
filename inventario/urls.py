from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),

]
