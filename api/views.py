from rest_framework.views import APIView

from api.models import EfoTerm, EfoTermSynonym, EfoTermOntology
from rest_framework import viewsets, status
from api.serializers import EfoTermSerializer, EfoTermSynonymSerializer, EfoTermOntologySerializer
from api.services import Services


class EfoTermViewSet(viewsets.ModelViewSet):
    queryset = EfoTerm.objects.all()
    serializer_class = EfoTermSerializer


class EfoTermSynonymViewSet(viewsets.ModelViewSet):
    queryset = EfoTermSynonym.objects.all()
    serializer_class = EfoTermSynonymSerializer


class EfoTermOntologyViewSet(viewsets.ModelViewSet):
    queryset = EfoTermOntology.objects.all()
    serializer_class = EfoTermOntologySerializer


class LoadEfoTermsView(APIView):
    def post(self, request):
        services = Services()

        return services.load_efo_terms_from_external_api()

