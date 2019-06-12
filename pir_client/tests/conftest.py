def pytest_configure():
    from django.conf import settings
    settings.configure(
        PFP_API_CLIENT_BASE_URL='http://none',
        PFP_API_CLIENT_API_KEY='test-api-key',
        PFP_API_CLIENT_SENDER_ID='test-sender',
        PFP_API_CLIENT_DEFAULT_TIMEOUT=5,
    )
