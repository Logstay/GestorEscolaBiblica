from django.db import models


class Aluno(models.Model):
    SEXO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    SALA_CHOICES = [
        ('Obreiro', 'Obreiros'),
        ('Mulheres', 'Mulheres'),
        ('Jovens', 'Jovens'),
        ('Discipulado', 'Discipulado')

    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    niver_data = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    sala = models.CharField(max_length=20, choices=SALA_CHOICES, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)


class Chamada(models.Model):
    CHAMADA_CHOICES = [
        ('P', 'PRESENTE'),
        ('F', 'FALTA'),
    ]
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(null=False, blank=False)
    chamada_aluno = models.CharField(max_length=1, choices=CHAMADA_CHOICES, null=False, blank=False)










    def __str__(self):
        return self.nome

