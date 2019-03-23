from .common import *

DEBUG = True
ALLOWED_HOSTS = ['django']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME','cat'),
        'USER': os.environ.get('DB_USER','postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD','postgres'),
        'HOST': os.environ.get('DB_HOST','localhost')
    },
}

INSTALLED_APPS += [
    'corsheaders'
]

CORS_ORIGIN_ALLOW_ALL = True

