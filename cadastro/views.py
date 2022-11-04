from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Cliente,Produto
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','preco','codigo', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('home')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome','idade','endereco','produto']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('home')