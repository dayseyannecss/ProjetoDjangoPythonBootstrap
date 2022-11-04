from django.urls import path
from .views import ProdutoCreate, ClienteCreate
from .views import ProdutoUpdate, ClienteUpdate
from .views import ProdutoDelete, ClienteDelete
from .views import ProdutoList, ClienteList

urlpatterns = [
    path("produto", ProdutoCreate.as_view(), name="cadastroproduto"),
    path("cliente", ClienteCreate.as_view(), name="cadastrocliente"),

    path("editar/cliente/<int:pk>", ClienteUpdate.as_view(), name="editarcliente"),
    path("editar/produto/<int:pk>", ProdutoUpdate.as_view(), name="editarProduto"),

    path("delete/cliente/<int:pk>", ClienteDelete.as_view(), name="deletarcliente"),
    path("delete/produto/<int:pk>", ProdutoDelete.as_view(), name="deletarProduto"),

    path("lista/cliente", ClienteList.as_view(), name="listcliente"),
    path("lista/produto", ProdutoList.as_view(), name="listProduto"),
]
