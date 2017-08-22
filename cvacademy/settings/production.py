from cvacademy.settings.base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
INSTALLED_APPS += (
    # other apps for production site
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
