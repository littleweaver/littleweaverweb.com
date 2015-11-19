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
    ('Dancerfly Support', 'support@dancerfly.com'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ pillar["deploy"]["secret_key"] }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {% if pillar['deploy']['debug'] %}True{% else %}False{% endif %}

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

MEDIA_ROOT = '{{ pillar["files"]["media_dir"] }}'
MEDIA_URL = '/media/'

DEFAULT_FROM_EMAIL = '{{ pillar["deploy"]["default_from_email"] }}'
SERVER_EMAIL = '{{ pillar["deploy"]["server_email"] }}'

GOOGLE_ANALYTICS_UA = 'UA-52154832-3'
GOOGLE_ANALYTICS_DOMAIN = 'littleweaverweb.com'

AWS_STORAGE_BUCKET_NAME = "{{ pillar['deploy']['s3_bucket_name'] }}"
AWS_ACCESS_KEY_ID = "{{ pillar['deploy']['aws_access_key_id'] }}"
AWS_SECRET_ACCESS_KEY = "{{ pillar['deploy']['aws_secret_access_key'] }}"

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
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
