from operator import imod
from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioCreationForm

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
    return render(request, 'perfil.html')


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