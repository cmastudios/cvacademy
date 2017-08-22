from cvacademy.settings.base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

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

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 0
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['cmastudios.me']