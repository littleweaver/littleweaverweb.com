# encoding: utf-8
"""
Django settings for webproject project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from littleweaverweb.settings.production import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
    ('Little Weaver', 'hello@littleweaverweb.com'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ pillar["deploy"]["secret_key"] }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {% if pillar['deploy']['debug'] %}True{% else %}False{% endif %}

ALLOWED_HOSTS = ['{{ pillar["deploy"]["server_name"] }}']

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ pillar["connections"]["db"]["name"] }}',
        'USER': '{{ pillar["connections"]["db"]["user"] }}',
        'PASSWORD': '{{ pillar["connections"]["db"]["password"] }}',
        'HOST': '{{ pillar["connections"]["db"]["host"] }}',
        'PORT': '{{ pillar["connections"]["db"]["port"] }}',
    }
}

DEFAULT_FROM_EMAIL = '{{ pillar["deploy"]["default_from_email"] }}'
SERVER_EMAIL = '{{ pillar["deploy"]["server_email"] }}'
MANDRILL_API_KEY = '{{ pillar["deploy"]["mandrill_api_key"] }}'
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

GOOGLE_ANALYTICS_UA = 'UA-52154832-3'
GOOGLE_ANALYTICS_DOMAIN = 'littleweaverweb.com'

AWS_STORAGE_BUCKET_NAME = "{{ pillar['deploy']['s3_bucket_name'] }}"
AWS_ACCESS_KEY_ID = "{{ pillar['deploy']['aws_access_key_id'] }}"
AWS_SECRET_ACCESS_KEY = "{{ pillar['deploy']['aws_secret_access_key'] }}"
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s %(levelname)s] %(message)s",
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{{ pillar["files"]["logs"]["django_file"] }}',
            # Max size: 2MB
            'maxBytes': 2 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'littleweaverweb': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
