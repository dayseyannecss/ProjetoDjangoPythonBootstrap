from django.urls import path
from .views import Index , Modelo

urlpatterns = [
    path('', Index.as_view(), name ='inicio'),
    path('modelo', Modelo.as_view() , name ='modelo'),
]
