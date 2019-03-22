from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME','test_db'),
        'USER': os.environ.get('DB_USER','test'),
        'PASSWORD': os.environ.get('DB_PASSWORD','test'),
        'HOST': os.environ.get('DB_HOST','localhost')
    },
}

INSTALLED_APPS += [
    'corsheaders'
]

CORS_ORIGIN_ALLOW_ALL = True
