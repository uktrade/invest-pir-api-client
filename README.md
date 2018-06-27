# Invest PIR API Client

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
