from django.urls import path
from views.login import views

urlpatterns = [
    path('login', views.login, name='login')
]
