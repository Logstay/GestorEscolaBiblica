from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('listar', listar_alunos, name='listar_alunos'),
    path('cadastrar', inserir_alunos, name='cadastrar_alunos'),
    path('listar/<int:id>', listar_alunos_id, name='listar_alunos_id'),
    path('editar/<int:id>', editar_aluno, name='editar_aluno'),
    path('remover/<int:id>', remover_alunos, name='remover_aluno'),
    path('accounts/login/home/', home, name='home'),
    path('accounts/login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]