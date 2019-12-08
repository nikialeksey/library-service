from .base import *

DEBUG = True

ALLOWED_HOSTS = ['192.168.99.100']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_pass',
        'HOST': 'db_leader',
        'PORT': 5432,
    },
    'follower': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_pass',
        'HOST': 'db_follower',
        'PORT': 5432,
    },
}

DATABASE_ROUTERS = ['service.router.LeaderFollowerRouter']
