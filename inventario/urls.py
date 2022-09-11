from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),

    # API
    path('api/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
