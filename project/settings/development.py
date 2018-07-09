from .defaults import *

DEBUG = True

INTERNAL_IPS = (
    '127.0.0.1'
)

# Add your domain name below
ALLOWED_HOSTS = ['localhost', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
