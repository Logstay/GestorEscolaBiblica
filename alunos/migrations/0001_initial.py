# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('niver_data', models.DateField()),
                ('telefone', models.CharField(max_length=11)),
                ('sala', models.CharField(max_length=20, choices=[('O', 'Obreiros'), ('M', 'Mulheres'), ('J', 'Jovens'), ('D', 'Discipulado')])),
                ('sexo', models.CharField(max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')])),
            ],
        ),
    ]
