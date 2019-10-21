from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

from .entidades import aluno
from .models import Aluno
from .forms import AlunoForm
from .services import aluno_service


# listando alunos
def listar_alunos(request):
    alunos = aluno_service.listar_aluno()
    return render(request, 'alunos/cadastrados.html', {'alunos': alunos})





# inserindo alunos
def inserir_alunos(request):
    ''' metodo insetir aluno form <- recebendo metodo ( AlunosForm() )
         que retorna 'Renderisando' passando a instancia para o template form_alunos.html '''
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sexo = form.cleaned_data['sexo']
            niver_data = form.cleaned_data['niver_data']
            telefone = form.cleaned_data['telefone']
            sala = form.cleaned_data['sala']
            novo_aluno = aluno.Aluno(nome=nome, sexo=sexo, niver_data=niver_data, telefone=telefone, sala=sala)
            aluno_service.cadastrar_aluno(novo_aluno)
            return redirect('listar_alunos')
    else:
        form_coisa = AlunoForm()
    return render(request, 'alunos/cadastrar_alunos.html', {'form': form_coisa})


def listar_alunos_id(request,id):
    aluno = aluno_service.listar_aluno_id(id)
    return render(request, 'alunos/lista_de_aluno.html', {'aluno': aluno})


def editar_aluno(request, id):
    aluno_a = aluno_service.listar_aluno_id(id)
    form = AlunoForm(request.POST or None, instance=aluno_a)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data['sexo']
        niver_data = form.cleaned_data['niver_data']
        telefone = form.cleaned_data['telefone']
        sala = form.cleaned_data['sala']
        novo_aluno = aluno.Aluno(nome=nome, sexo=sexo, niver_data=niver_data, telefone=telefone, sala=sala)
        aluno_service.editar_aluno(aluno_a, novo_aluno)
        return redirect('listar_alunos')
    return render(request, 'alunos/cadastrar_alunos.html', {'form': form})


def remover_alunos(request, id):
    aluno = aluno_service.listar_aluno_id(id)
    if request.method == 'POST':
        aluno_service.remover_aluno(aluno)
        return redirect('listar_alunos')
    return render(request, 'alunos/confirm_exclusao.html', {'aluno': aluno})


def home(request):
    return render(request, 'alunos/home.html')




def login(request):
    return render(request, 'registration/login.html')


def cadastar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('usuario/home.html')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuario/login.html', {'form_usuario': form_usuario})


def cadastro(request):
    return render(request, 'usuario/cadastro_usuario.html')