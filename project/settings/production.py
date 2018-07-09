from .defaults import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

INTERNAL_IPS = (
    '127.0.0.1'
)

# Add your domain name below
ALLOWED_HOSTS = ['localhost', '0.0.0.0']

# Put your DB name, user and password
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
