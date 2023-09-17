import requests
import logging

from django.db import DatabaseError
from rest_framework.response import Response
from api.models import EfoTerm, EfoTermSynonym, EfoTermOntology
from django.conf import settings
from rest_framework import status


class Services:
    EMBEDDED_STRING = '_embedded'
    TERMS_STRING = 'terms'
    TERM_ID_STRING = 'obo_id'
    LABEL_STRING = 'label'
    SYNONYMS_STRING = 'synonyms'
    LINKS_STRING = '_links'
    IS_ROOT_STRING = 'is_root'
    PARENT_TERMS_STRING = 'parents'

    def load_efo_terms_from_external_api(self):
        api_response = requests.get(settings.LOAD_EFO_DATA_URL)

        if api_response.status_code != 200:
            logging.error('Failed to access the external API')
            return Response({'message': 'Failed to access the external API'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            logging.info('Start adding EFO terms to the database')
            self.recursively_add_efo_terms_to_database(api_response.json())
            logging.info('Successfully added EFO terms to the database')
            return Response({'message': 'Successfully added EFO terms to the database'},
                            status=status.HTTP_200_OK)
        except ValueError as e:
            logging.error(f'Failed parsing JSON data from the API response: {str(e)}')
            return Response({'message': 'Failed parsing JSON data from the API response'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DatabaseError as e:
            logging.error(f'Failed to add EFO terms due to a database error: {str(e)}')
            return Response({'message': 'Failed to add EFO terms due to a database error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logging.error(f'Failed to add EFO terms due to unexpected error: {str(e)}')
            return Response({'message': 'Failed to add EFO terms due to unexpected error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def recursively_add_efo_terms_to_database(self, terms_json_response, child_term_object=None):
        for term_json in terms_json_response[self.EMBEDDED_STRING][self.TERMS_STRING]:
            term_has_parent = not term_json[self.IS_ROOT_STRING]

            term_object = self.add_and_retrieve_efo_term_object_from_database(term_json)
            self.add_efo_term_synonym_object_to_database(term_json, term_object)

            if child_term_object:
                self.add_efo_term_ontology_object_to_database(term_object, child_term_object)

            if term_has_parent:
                parent_terms_json_response = self.get_efo_terms_json_response(term_json)

                self.recursively_add_efo_terms_to_database(parent_terms_json_response, term_object)

    def get_efo_terms_json_response(self, term):
        api_response = requests.get(term[self.LINKS_STRING][self.PARENT_TERMS_STRING]['href'])
        return api_response.json()

    def add_and_retrieve_efo_term_object_from_database(self, efo_term):
        term_object, _ = EfoTerm.objects.get_or_create(
            term_id=efo_term[self.TERM_ID_STRING], label=efo_term[self.LABEL_STRING])

        return term_object

    def add_efo_term_synonym_object_to_database(self, term_json, term_object):
        for synonym in term_json[self.SYNONYMS_STRING]:
            EfoTermSynonym.objects.get_or_create(efo_term=term_object, synonym=synonym)

    def add_efo_term_ontology_object_to_database(self, parent_efo_object, child_efo_term_object):
        EfoTermOntology.objects.get_or_create(
            parent_efo_term=parent_efo_object, child_efo_term=child_efo_term_object)
