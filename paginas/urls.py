from django.urls import path
from .views import Index , Modelo

urlpatterns = [
    path('', Index.as_view(), name ='home'),
    path('cart', Modelo.as_view() , name ='cart'),
]
