# Generated by Django 5.0.2 on 2024-03-30 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_remove_curriculo_funcao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=100)),
                ('experiencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.experiencia')),
            ],
        ),
    ]
