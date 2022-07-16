from django.urls import path
from views.login import views as views_login
from views.cadastro import views as views_cadastro
from views.logout import views as views_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views_login.login, name='login'),
    path('cadastro', views_cadastro.cadastro, name='cadastro'),
    path('logout', views_logout.sair, name='logout'),
    path('deletar_usuario', views_cadastro.deleta_usuario, name='deletar_usuario'),
    path('suspender_usuario', views_cadastro.suspende_usuario, name='suspender_usuario'),
    path('ativar_usuario', views_cadastro.ativa_usuario, name='ativar_usuario'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
