from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "home_page.html", context)

def sobre(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "sobre.html", context)