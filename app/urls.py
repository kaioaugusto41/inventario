from django.urls import path
from views.index import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('impressoras', views.impressoras, name='impressoras'),
    path('logs', views.logs, name='logs'),
    path('logs_entrada_toner', views.logs_entrada_toner, name='logs_entrada_toner'),
    path('logs_saida_toner', views.logs_saida_toner, name='logs_saida_toner'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('todas_as_solicitacoes', views.todas_as_solicitacoes, name='todas_as_solicitacoes'),
    path('solicitacoes_em_aberto', views.solicitacoes_em_aberto, name='solicitacoes_em_aberto'),
    path('solicitacoes_encerradas', views.solicitacoes_encerradas, name='solicitacoes_encerradas')
]