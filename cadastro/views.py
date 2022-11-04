from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente,Produto
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','preco','codigo', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listProduto')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome','idade','endereco','produto']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listcliente')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'preco', 'codigo', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listProduto')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome','idade','endereco','produto']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listcliente')

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'cadastro/formDelete.html'
    success_url = reverse_lazy('listProduto')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastro/formDelete.html'
    success_url = reverse_lazy('listcliente')

class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastro/ListaProduto.html'


class ClienteList(ListView):
    model = Cliente
    template_name = 'cadastro/listaCliente.html'
