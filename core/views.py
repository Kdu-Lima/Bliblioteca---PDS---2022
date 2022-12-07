from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required

def teste(request):
    return render(request, 'teste.html')

def T_inicial(request):
    return render(request, 'index.html')

def registro(request):

    # if form.is_valid():
    #     form.save()
    #     return redirect('inicio')

    return render(request, 'registro.html')

def base(request):
    return render(request, 'base.html')

def aut(request):
    return render(request, 'index_auth.html')

def login(request):
    return render(request, 'login.html')

@login_required
def perfil(request):
    return render(request, 'perfil,html')
