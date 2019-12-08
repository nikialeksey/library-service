from .base import *

DEBUG = True

ALLOWED_HOSTS = ['192.168.99.100']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db_1',
        'PORT': 5432,
    }
}
