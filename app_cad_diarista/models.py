from django.db import models

class Diarista(models.Model):
    id_diarista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    setor = models.PositiveIntegerField()
    rg = models.CharField(max_length=12, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.EmailField(default="")
    telefone = models.CharField(max_length=11, null=False)
    pix = models.TextField(max_length=100, null=False)

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=18, null=False)
    estado = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    rua = models.CharField(max_length=100, null=False)
    numero = models.TextField(max_length=4, null=False)
    email = models.EmailField(default="")
    cep = models.CharField(max_length=9, null= False)