from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-ip-address', 'your-host-domain-name']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT"),
    }
}

STRIP_PUBLIC_KEY = config('STRIP_PUBLIC_KEY')
STRIP_SECRET_KEY = config('STRIP_SECRET_KEY')