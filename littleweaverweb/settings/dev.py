from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'NOTSECRET'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
