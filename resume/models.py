from django.db import models
from users.models import CustomUser

class Curriculo(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    funcao = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.nome} | {self.user}'

class Ensino(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    instituicao = models.CharField(max_length = 100)
    destaque = models.TextField()
    inicio = models.DateField()
    termino = models.DateField()

    def __str__(self):
        return f'{self.nome} | {self.curriculo}'

class Emprego(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    empresa = models.CharField(max_length = 100)
    cargo = models.CharField(max_length = 100)
    funcoes = models.TextField()
    destaque = models.TextField()
    inicio = models.DateField()
    termino = models.DateField()

    def __str__(self):
        return f'{self.empresa} - {self.cargo} | {self.curriculo}'
    
class Projeto(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)
    inicio = models.DateField()
    termino = models.DateField()

    def __str__(self):
        return f'{self.nome} | {self.curriculo}'