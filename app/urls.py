from django.urls import path
from views.index import views

urlpatterns = [
    path('', views.index, name='index')
]