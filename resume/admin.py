from django.contrib import admin
from .models import Curriculo, Ensino, Emprego, Projeto

# Register your models here.
admin.site.register(Curriculo)
admin.site.register(Ensino)
admin.site.register(Emprego)
admin.site.register(Projeto)