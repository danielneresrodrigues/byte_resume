from django.db import models
from users.models import CustomUser

class Curriculo(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    objetivo = models.TextField()

    def __str__(self):
        return f'{self.nome} | {self.user}'

class FormacaoAcademica(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    curso = models.CharField(max_length = 100)
    instituicao = models.CharField(max_length = 100)
    cidade = models.CharField(max_length = 100)
    inicio = models.DateField()
    termino = models.DateField(blank = True, null = True)
    presente = models.BooleanField()

    def __str__(self):
        return f'{self.curso} | {self.curriculo}'

class Experiencia(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    cargo = models.CharField(max_length = 100)
    empresa = models.CharField(max_length = 100)
    inicio = models.DateField()
    termino = models.DateField(blank = True, null = True)
    presente = models.BooleanField()

    def __str__(self):
        return f'{self.cargo} - {self.empresa} | {self.curriculo}'
    
class Funcao(models.Model):

    experiencia = models.ForeignKey(Experiencia, on_delete = models.CASCADE)
    funcao = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.funcao} | {self.experiencia}'
    
class Projeto(models.Model):

    curriculo = models.ForeignKey(Curriculo, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    instituicao = models.CharField(max_length = 100)
    descricao = models.TextField()
    periodo = models.DateField()

    def __str__(self):
        return f'{self.nome} | {self.curriculo}'