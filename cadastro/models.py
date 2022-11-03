from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=250, verbose_name='Descrição')
    preco = models.FloatField(verbose_name="Preço")
    codigo = models.FloatField(verbose_name="Código")

    def __str__(self):
        return "{} ({})".format(self.nome,self.preco, self.descricao)

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=250, verbose_name='Endereço')
    idade = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.nome,self.idade, self.endereco, self.produto )