from django.shortcuts import render

# Create your views here.]

def home(request):
    return render(request, 'home.html')

def contatos(resquest):
    return render(resquest, 'contatos.html')
