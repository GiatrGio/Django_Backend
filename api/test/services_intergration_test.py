import unittest
from api.services import Services
from django.test import TestCase


class ServicesIntegrationTestCase(TestCase):
    def setUp(self):
        self.services_instance = Services()

    def test_load_efo_terms_from_external_api(self):
        """Test the results from all the parts inside this method"""
        pass


if __name__ == '__main__':
    unittest.main()
