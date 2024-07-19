from rest_framework import serializers
from .models import Candidatura, Cliente, Recrutador, Vaga, Candidato

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email']

class RecrutadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recrutador
        fields = ['id', 'nome', 'email', 'telemovel']

class VagaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    recrutador = RecrutadorSerializer()

    class Meta:
        model = Vaga
        fields = ['id', 'titulo', 'descricao', 'data_publicacao', 'cliente', 'recrutador']

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id', 'nome', 'email', 'telemovel']

class CandidaturaSerializer(serializers.ModelSerializer):
    candidato = CandidatoSerializer()
    vaga = VagaSerializer()

    class Meta:
        model = Candidatura
        fields = ['id', 'candidato', 'vaga', 'data_candidatura', 'estado']
