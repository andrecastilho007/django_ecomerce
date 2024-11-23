from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

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

def contato(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página contato",
        "content": "Bem-vindo a página contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('Nome_Completo'))
        print(request.POST.get('email'))
        print(request.POST.get('Mensagem'))
    return render(request, "contato.html", context)