from django.shortcuts import render


def index(request):
    contexto = {
        'Curso': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html', contexto)


def contato(request):
    return render(request, 'contato.html')