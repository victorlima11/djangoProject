from django.shortcuts import render

# Create your views here.]

def home(request):
    return render(request, 'home.html')

def contatos(resquest):
    return render(resquest, 'contatos.html')

def blog(request):
    return render(request, 'blog.html')

def enderecos(request):
    return render(request, 'enderecos.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def sobre(request):
    return render(request, 'sobre.html')