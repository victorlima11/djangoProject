from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
    path('enderecos/', views.enderecos, name='enderecos'),
    path('blog/', views.blog, name='blog'),
    path('sobre/', views.sobre, name='sobre'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('cadastro_cliente/', views.cadastrar_cliente, name='cadastro_cliente'),
    path('cadastro_produto/', views.cadastrar_produto, name='cadastro_produto'),
    path('pedido/', views.pedido, name='pedido')
]