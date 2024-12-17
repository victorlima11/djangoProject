from django.shortcuts import render
from .models import Cliente, Produto, Pedido

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

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        Cliente.objects.create(nome=nome, telefone=telefone, email=email)

    return render(request, 'cadastro_cliente.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')

        Produto.objects.create(nome=nome, quantidade=quantidade)
    return render(request, 'cadastro_produto.html')

from django.shortcuts import render, redirect
from .models import Cliente, Produto, Pedido
from django.http import HttpResponse

def pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        # Verificar se o cliente existe
        if not Cliente.objects.filter(id=cliente_id).exists():
            return HttpResponse("Cliente não encontrado.", status=404)
        
        # Verificar se o produto existe
        if not Produto.objects.filter(id=produto_id).exists():
            return HttpResponse("Produto não encontrado.", status=404)

        # Recuperar os objetos cliente e produto
        cliente = Cliente.objects.get(id=cliente_id)
        produto = Produto.objects.get(id=produto_id)

        # Criar o pedido
        Pedido.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)

        # Redirecionar ou renderizar a página com clientes e produtos
        return redirect('sucesso_pedido')  # Substitua com a URL desejada de sucesso

    # Caso a requisição seja GET, carregamos os clientes e produtos
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'pedido.html', {'clientes': clientes, 'produtos': produtos})
