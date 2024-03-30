from django.contrib import admin
from .models import Curriculo, FormacaoAcademica, Experiencia, Funcao, Projeto

# Register your models here.
admin.site.register(Curriculo)
admin.site.register(FormacaoAcademica)
admin.site.register(Experiencia)
admin.site.register(Funcao)
admin.site.register(Projeto)