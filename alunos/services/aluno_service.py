from ..models import Aluno
from django.db import connection


def listar_aluno():
    alunos = Aluno.objects.all()
    return alunos


def listar_aluno_id(id):
    alunos = Aluno.objects.get(id=id)
    return alunos


def remover_aluno(aluno):
    aluno.delete()


def cadastrar_aluno(aluno):
    Aluno.objects.create(nome=aluno.nome, sexo=aluno.sexo, niver_data=aluno.niver_data, telefone=aluno.telefone,
                         sala=aluno.sala)


def editar_aluno(aluno, novo_aluno):
    aluno.nome = novo_aluno.nome
    aluno.sexo = novo_aluno.sexo
    aluno.niver_data = novo_aluno.niver_data
    aluno.telefone = novo_aluno.telefone
    aluno.sala = novo_aluno.sala
    aluno.save(force_update=True)
