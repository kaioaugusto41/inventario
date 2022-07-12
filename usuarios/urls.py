from django.urls import path
from views.login import views as views_login
from views.cadastro import views as views_cadastro
from views.logout import views as views_logout

urlpatterns = [
    path('', views_login.login, name='login'),
    path('cadastro', views_cadastro.cadastro, name='cadastro'),
    path('logout', views_logout.sair, name='logout'),
    path('deletar_usuario', views_cadastro.deleta_usuario, name='deletar_usuario'),
    path('suspender_usuario', views_cadastro.suspende_usuario, name='suspender_usuario'),
    path('ativar_usuario', views_cadastro.ativa_usuario, name='ativar_usuario'),
]
