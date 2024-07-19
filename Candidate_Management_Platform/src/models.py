from django.db import models


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Recrutador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telemovel = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_publicacao = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    recrutador = models.ForeignKey(Recrutador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Candidato(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telemovel = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_candidatura = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('em_processo', 'Em Processo'),
        ('desqualificado', 'Desqualificado'),
        ('desistiu', 'Desistiu'),
        ('contratado', 'Contratado'),
    ]
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default='em_processo')

    def get_cliente(self):
        return self.vaga.cliente

    def get_recrutador(self):
        return self.vaga.recrutador

    def get_vaga(self):
        return self.vaga





