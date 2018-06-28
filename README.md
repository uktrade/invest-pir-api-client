# Invest PIR API Client
[![CircleCI](https://circleci.com/gh/uktrade/invest-pir-api-client.svg?style=svg)](https://circleci.com/gh/uktrade/invest-pir-api-client)
[![codecov](https://codecov.io/gh/uktrade/invest-pir-api-client/branch/master/graph/badge.svg)](https://codecov.io/gh/uktrade/invest-pir-api-client)

Client for the PIR service (yet to be deployed)

## Example 

    from pir_client.client import PIRAPIClient

    client = PIRAPIClient(
        base_url=settings.PIR_API_URL,
        api_key=settings.PIR_API_KEY
    )

    # Creates report and sends email
    client.create_report({
        'name': 'test',
        'sector': 'tech',
        'market': 'usa',
        'company': 'Acme',
        'email': 'foo@acme.com'
    })

## Install 

    pip install invest-pir-api-client
