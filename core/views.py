from operator import imod
from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioCreationForm

#Para os cruds:-----------------------------------------------------------------------------------------------------------------------------
from .models import Area, Avaliacao, Disciplina, Livro, Recomendacao, Subarea, Tipo, Usuario
from .forms import AreaForm, AvaliacaoForm, DisciplinaForm, LivroForm, RecomendacaoForm, SubareaForm, TipoForm
#-------------------------------------------------------------------------------------------------------------------------------------------

def teste(request):
    return render(request, 'teste.html')

def T_inicial(request):
    return render(request, 'index.html')

def registro(request):
    form = UsuarioCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
    'form': form
    }
    return render(request, 'registro.html', contexto)

def base(request):
    return render(request, 'base.html')

def aut(request):
    return render(request, 'index_auth.html')

def login(request):
    return render(request, 'login.html')

@login_required
def perfil(request):
    usuario =       Usuario.objects.all
    contexto = {
        'todos_tipos': usuario
    }
    return render(request, 'perfil.html', contexto)


def cadastro_manual(request):
    user = Usuario.objects.create_user(
        username='admin',
        email='admin@email.com',
        nome='Administrador',
        password='123',
        is_superuser=True
    )
    user.save()
    return redirect('inicial')

#CRUDS---------------------------------------------------------------------------------------------------------------------------------------

def listar_tipo(request):
    tipos = Tipo.objects.all
    contexto = {
        'todos_tipos': tipos
    }
    return render(request, 'cruds/tipo.html', contexto)

def listar_disciplina(request):
    disciplinas = Disciplina.objects.all
    contexto = {
        'todas_disciplinas': disciplinas
    }
    return render(request, 'cruds/disciplina.html', contexto)

def listar_livro(request):
    livros = Livro.objects.all
    contexto = {
        'todos_livros': livros
    }
    return render(request, 'cruds/livro.html', contexto)


def listar_area(request):
    areas = Area.objects.all
    contexto = {
        'todas_areas': areas
    }
    return render(request, 'cruds/area.html', contexto)

def listar_usuario(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'todos_usuarios': usuarios
    }
    return render(request, 'cruds/usuario.html', contexto)

def listar_subarea(request):
    subareas = Subarea.objects.all
    contexto = {
        'todas_subareas': subareas
    }
    return render(request, 'cruds/subarea.html', contexto)

def listar_recomendacao(request):
    recomendacoes = Recomendacao.objects.all
    contexto = {
        'todas_recomendacoes': recomendacoes
    }
    return render(request, 'cruds/recomendacao.html', contexto)

def listar_avaliacao(request):
    avaliacoes = Avaliacao.objects.all
    contexto = {
        'todas_avaliacoes': avaliacoes
    }
    return render(request, 'cruds/avaliacao.html', contexto)




def cadastrar_tipo(request):
    form = TipoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_tipo')

    contexto = {
        'form_tipo': form
    }
    return render(request, 'cruds/tipo_cadastrar.html', contexto)

def cadastrar_disciplina(request):
    form = DisciplinaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_disciplina')

    contexto = {
        'form_disciplina': form
    }
    return render(request, 'cruds/disciplina_cadastrar.html', contexto)

def cadastrar_livro(request):
    form = LivroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        livro = form.save(commit=False)
        livro.usuario = request.user
        livro.save()
        return redirect('listar_livro')

    contexto = {
        'form_livro': form
    }
    
    return render(request, 'cruds/livro_cadastrar.html', contexto)

def cadastrar_area(request):
    form = AreaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_area')

    contexto = {
        'form_area': form
    }
    return render(request, 'cruds/area_cadastrar.html', contexto)

def cadastrar_usuario(request):
    form = UsuarioCreationForm (request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_usuario')

    contexto = {
        'form_usuarios': form
    }
    return render(request, 'cruds/usuario_cadastrar.html', contexto)

def cadastrar_subarea(request):
    form = SubareaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_subarea')

    contexto = {
        'form_subarea': form
    }
    return render(request, 'cruds/subarea_cadastrar.html', contexto)

def cadastrar_recomendacao(request):
    form = RecomendacaoForm(request.POST or None)
    
    if form.is_valid():
        recomendacao = form.save(commit=False)
        recomendacao.usuario = request.user
        recomendacao.save()
        return redirect('listar_recomendacao')

    contexto = {
        'form_recomendacao': form
    }
    return render(request, 'cruds/recomendacao_cadastrar.html', contexto)



def cadastrar_avaliacao_livros(request):
    todos_recomendacoes = Recomendacao.objects.all()
    contexto = {
        'todos_recomendacoes': todos_recomendacoes
    }
    return render(request, 'cruds/avaliacao_cadastrar_livros.html', contexto)


def cadastrar_avaliacao(request, id):
    form = AvaliacaoForm(request.POST or None)
    recomendacao = Recomendacao.objects.get(pk=id)
    if form.is_valid():
        avaliacao = form.save(commit=False)
        avaliacao.usuario = request.user
        id_recomendacao = request.POST['recomendacao_id']
        avaliacao.id_recomendacao = Recomendacao.objects.get(pk=id_recomendacao)
        avaliacao.save()
        return redirect('listar_avaliacao')

    contexto = {
        'form_avaliacao': form,
        'recomendacao': recomendacao,
    }
    return render(request, 'cruds/avaliacao_cadastrar.html', contexto)











def editar_tipo(request, id):
    tipo = Tipo.objects.get(pk=id)

    form = TipoForm(request.POST or None, instance=tipo)

    if form.is_valid():
        form.save()
        return redirect('listar_tipo')

    contexto = {
        'form_tipo': form
    }
    return render(request, 'cruds/tipo_cadastrar.html', contexto)

def editar_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    
    if form.is_valid():
        form.save()
        return redirect('listar_disciplina')

    contexto = {
        'form_disciplina': form
    }
    return render(request, 'cruds/disciplina_cadastrar.html', contexto)

def editar_livro(request, isbn):
    livro = Livro.objects.get(pk=isbn)

    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('listar_livro')
    
    contexto = {
        'form_livro': form
    }
    return render(request, 'cruds/livro_cadastrar.html', contexto)

def editar_area(request, id):
    area = Area.objects.get(pk=id)

    form = AreaForm(request.POST or None, instance=area)
    
    if form.is_valid():
        form.save()
        return redirect('listar_area')

    contexto = {
        'form_area': form
    }
    return render(request, 'cruds/area_cadastrar.html', contexto)

def editar_usuario(request, username):
    usuario = Usuario.objects.get(pk=username)

    form = UsuarioCreationForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('listar_usuario')

    contexto = {
        'form_usuarios': form
    }

    return render(request, "cruds/usuario_cadastrar.html", contexto)

def editar_subarea(request, id):
    subarea = Subarea.objects.get(pk=id)

    form = SubareaForm(request.POST or None, instance=subarea)
    
    if form.is_valid():
        form.save()
        return redirect('listar_subarea')

    contexto = {
        'form_subarea': form
    }
    return render(request, 'cruds/subarea_cadastrar.html', contexto)

def editar_recomendacao(request, id):
    recomendacao = Recomendacao.objects.get(pk=id)

    form = RecomendacaoForm(request.POST or None, instance=recomendacao)
    
    if form.is_valid():
        form.save()
        return redirect('listar_recomendacao')

    contexto = {
        'form_recomendacao': form
    }
    return render(request, 'cruds/recomendacao_cadastrar.html', contexto)

def editar_avaliacao(request, id):
    avaliacao = Avaliacao.objects.get(pk=id)

    form = AvaliacaoForm(request.POST or None, instance=avaliacao)
    
    if form.is_valid():
        form.save()
        return redirect('listar_avaliacao')

    contexto = {
        'form_avaliacao': form,
        'recomendacao': avaliacao.id_recomendacao
    }
    return render(request, 'cruds/avaliacao_cadastrar.html', contexto)





def remover_tipo(request, id):
    tipo = Tipo.objects.get(pk=id)
    tipo.delete()
    return redirect('listar_tipo')

def remover_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    disciplina.delete()
    return redirect('listar_disciplina')

def remover_livro(request, isbn):
    livro = Livro.objects.get(pk=isbn)
    livro.delete()
    return redirect('listar_livro')

def remover_area(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('listar_area')

def remover_usuario(request, username):
    usuario = Usuario.objects.get(pk=username)
    usuario.delete()
    return redirect('listar_usuario')

def remover_subarea(request, id):
    subarea = Subarea.objects.get(pk=id)
    subarea.delete()
    return redirect('listar_subarea')

def remover_recomendacao(request, id):
    recomendacao = Recomendacao.objects.get(pk=id)
    recomendacao.delete()
    return redirect('listar_recomendacao')

def remover_avaliacao(request, id):
    avaliacao = Avaliacao.objects.get(pk=id)
    avaliacao.delete()
    return redirect('listar_avaliacao')