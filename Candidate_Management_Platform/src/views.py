from rest_framework import viewsets
from .models import Cliente, Recrutador, Vaga, Candidato, Candidatura
from .serializers import ClienteSerializer, RecrutadorSerializer, VagaSerializer, CandidatoSerializer, CandidaturaSerializer
from rest_framework.decorators import action

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class RecrutadorViewSet(viewsets.ModelViewSet):
    queryset = Recrutador.objects.all()
    serializer_class = RecrutadorSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

    
class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer


    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        candidatura = self.get_object()
        status = request.data.get('status')
        if status not in dict(Candidatura.STATUS_CHOICES).keys():
            return Response({'error': 'Invalid status'}, status=400)
        candidatura.estado = status
        candidatura.save()
        return Response(CandidaturaSerializer(candidatura).data)

        
    def get_queryset(self):
        queryset = super().get_queryset()
        candidato_id = self.request.query_params.get('candidato', None)
        if candidato_id:
            queryset = queryset.filter(candidato_id=candidato_id)
        return queryset





