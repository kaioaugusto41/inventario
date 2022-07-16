from django.urls import path
from views.index import views
from views.impressoras.views import impressoras
from views.logs.views import logs
from views.logs_entrada_toner.views import logs_entrada_toner
from views.logs_saida_toner.views import logs_saida_toner
from views.usuarios.views import usuarios
from views.todas_as_solicitacoes.views import todas_as_solicitacoes
from views.solicitacoes_em_aberto.views import solicitacoes_em_aberto
from views.solicitacoes_encerradas.views import solicitacoes_encerradas
from views.minhas_solicitacoes.views import minhas_solicitacoes

urlpatterns = [
    path('index', views.index, name='index'),
    path('impressoras', impressoras, name='impressoras'),
    path('logs', logs, name='logs'),
    path('logs_entrada_toner', logs_entrada_toner, name='logs_entrada_toner'),
    path('logs_saida_toner', logs_saida_toner, name='logs_saida_toner'),
    path('usuarios', usuarios, name='usuarios'),
    path('todas_as_solicitacoes', todas_as_solicitacoes, name='todas_as_solicitacoes'),
    path('solicitacoes_em_aberto', solicitacoes_em_aberto, name='solicitacoes_em_aberto'),
    path('solicitacoes_encerradas', solicitacoes_encerradas, name='solicitacoes_encerradas'),
    path('minhas_solicitacoes', minhas_solicitacoes, name='minhas_solicitacoes')
]