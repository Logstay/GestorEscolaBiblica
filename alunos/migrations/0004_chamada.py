# Generated by Django 2.2.5 on 2019-09-24 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_auto_20190914_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('chamada_aluno', models.CharField(choices=[('P', 'PRESENTE'), ('F', 'FALTA')], max_length=1)),
                ('nome_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.Aluno')),
            ],
        ),
    ]
