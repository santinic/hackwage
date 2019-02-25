from .shared_settings import *

DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# STRIPE TEST ENV
STRIPE_PUBLIC_KEY = "pk_test_3b8p2tskf93SebgWBzDyNVpV"
STRIPE_SECRET_KEY = "sk_test_q2xZ9jHomTieALzwn54ceob0"
