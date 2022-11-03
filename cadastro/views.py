from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Cliente,Produto
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','endereco','preco','codigo']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('home')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome','descricao','idade','produto']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('home')