from django.urls import path
from .views import ProdutoCreate, ClienteCreate

urlpatterns = [
    path("produto", ProdutoCreate.as_view(), name="cadastroproduto"),
    path("cliente", ClienteCreate.as_view(), name="cadastrocliente"),
]
