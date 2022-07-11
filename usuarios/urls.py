from django.urls import path
from views.login import views as views_login
from views.cadastro import views as views_cadastro
from views.logout import views as views_logout

urlpatterns = [
    path('', views_login.login, name='login'),
    path('cadastro', views_cadastro.cadastro, name='cadastro'),
    path('logout', views_logout.sair, name='logout')
]
