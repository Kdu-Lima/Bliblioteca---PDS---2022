from django.shortcuts import render

def teste(request):
    return render(request, 'teste.html')

def T_inicial(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')
