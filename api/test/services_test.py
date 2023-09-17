import unittest
from django.test import TestCase
from api.models import EfoTerm, EfoTermSynonym, EfoTermOntology
from api.services import Services


class ServicesTestCase(TestCase):
    def setUp(self):
        self.services_instance = Services()
        self.efo_term_api_json_response = self.get_fake_efo_term_api_json_response()
        self.single_efo_term = self.efo_term_api_json_response['_embedded']['terms'][0]

    def test_add_efo_terms_json_to_database(self):
        self.services_instance.recursively_add_efo_terms_to_database(self.efo_term_api_json_response)

        self.assertEqual(EfoTerm.objects.count(), 1)
        self.assertEqual(EfoTermSynonym.objects.count(), 1)
        self.assertEqual(EfoTermOntology.objects.count(), 0)

    def test_add_efo_term_instance_to_database(self):
        efo_term_instance = self.services_instance.add_and_retrieve_efo_term_object_from_database(self.single_efo_term)

        self.assertEqual(efo_term_instance.term_id, self.single_efo_term['obo_id'])
        self.assertEqual(efo_term_instance.label, self.single_efo_term['label'])

    def test_add_efo_term_synonym_instance_to_database(self):
        """Similar as above, but for EfoTermSynonym"""
        pass

    def test_add_efo_term_ontology_instance_to_database(self):
        """Similar as above, but for EfoTermOntology"""
        pass

    @staticmethod
    def get_fake_efo_term_api_json_response():
        return {
            '_embedded': {
                'terms': [
                    {
                        'obo_id': 'EFO:0000001',
                        'label': 'disease',
                        'synonyms': [
                            'disease'
                        ],
                        'is_root': True,
                        'parents': []
                    }
                ]
            }
        }


if __name__ == '__main__':
    unittest.main()
