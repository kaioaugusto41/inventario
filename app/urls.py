from django.urls import path
from views.index import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('logs', views.logs, name='logs')
]