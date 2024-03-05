# Generated by Django 5.0.2 on 2024-03-04 23:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('funcoes', models.TextField()),
                ('destaque', models.TextField()),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='Ensino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=100)),
                ('destaque', models.TextField()),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.curriculo')),
            ],
        ),
    ]
