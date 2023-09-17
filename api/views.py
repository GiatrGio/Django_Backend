import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import DatabaseError
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

        try:
            services.load_efo_terms_from_external_api()
            return Response(status=status.HTTP_201_CREATED)
        except ValueError as e:
            logging.error(f'Failed parsing JSON data from the API response: {str(e)}')
            return Response({'message': 'Failed parsing JSON data from the API response'},
                            status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
            logging.error(f'Failed to add EFO terms due to a database error: {str(e)}')
            return Response({'message': 'Failed to add EFO terms due to a database error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logging.error(f'Failed to add EFO terms due to unexpected error: {str(e)}')
            return Response({'message': 'Failed to add EFO terms due to unexpected error'},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"message": "This endpoint only accepts POST requests."},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

