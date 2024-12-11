from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
    path('enderecos/', views.enderecos, name='enderecos'),
    path('blog/', views.blog, name='blog'),
    path('sobre/', views.sobre, name='sobre'),
    path('parceiros/', views.parceiros, name='parceiros')
]