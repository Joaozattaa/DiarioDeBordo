from django.db import models

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.placa})"

class RegistroUso(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    nome_usuario = models.CharField(max_length=100)
    destino = models.CharField(max_length=255)
    kilometragem_saida = models.IntegerField()
    kilometragem_chegada = models.IntegerField(blank=True, null=True)
    horario_saida = models.DateTimeField()
    horario_chegada = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Registro de {self.nome_usuario} no veículo {self.veiculo}"
