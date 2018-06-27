import httpretty
import json
import unittest

from unittest import TestCase

from pir_client.client import PIRAPIClient


OPTIONS_DATA = {
    "actions": {
        "POST": {
            "country": {
                "choices": [
                    {
                        "value": "AF",
                        "display_name": "Afghanistan"
                    },
                ]
            },

            "market": {
                "choices": [
                    {
                        "value": "africa",
                        "display_name": "africa"
                    },
                    {
                        "value": "canada",
                        "display_name": "canada"
                    }
                ]
            },
            "sector": {
                "choices": [
                    {
                        "value": "tech",
                        "display_name": "Technology"
                    },
                    {
                        "value": "automotive",
                        "display_name": "Automotive"
                    },
                ]
            }
        }
    }
}


class APIClientTestCase(TestCase):
    def setUp(self):
        httpretty.enable()
        httpretty.register_uri(
            httpretty.OPTIONS, "http://none/api/pir/",
            body=json.dumps(OPTIONS_DATA)
        )

        httpretty.register_uri(
            httpretty.POST, "http://none/api/pir/",
        )

    def tearDown(self):
        httpretty.disable()

    def test_post(self):
        client = PIRAPIClient(base_url='http://none', api_key='none')

        res = client.create_report({
            'name': 'test',
            'sector': 'tech',
            'market': 'africa',
            'company': 'Rollo',
            'email': 'rollokb@gmail.com'
        })

        self.assertIsInstance(res, dict)

        with self.assertRaises(ValueError):
            client.create_report({
                'name': 'test',
                'sector': 'tech',
                'market': 'not a market',
                'company': 'Rollo',
                'email': 'rollokb@gmail.com'
            })

        with self.assertRaises(ValueError):
            client.create_report({
                'name': 'test',
                'sector': 'tech',
                'country': 'not a country',
                'company': 'Rollo',
                'email': 'rollokb@gmail.com'
            })

        with self.assertRaises(ValueError):
            client.create_report({
                'name': 'test',
                'sector': 'tech',
                'country': 'AF',
                'market': 'africa',
                'company': 'Rollo',
                'email': 'rollokb@gmail.com'
            })


if __name__ == '__main__':
    unittest.main()
