from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

def teste(request):
    return render(request, 'teste.html')

def T_inicial(request):
    return render(request, 'inicial.html')

def registro(request):

    # if form.is_valid():
    #     form.save()
    #     return redirect('inicio')

    return render(request, 'registro.html')

def base(request):
    return render(request, 'base.html')
