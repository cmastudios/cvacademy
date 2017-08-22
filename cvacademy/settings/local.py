from cvacademy.settings.base import *

DEBUG = True
INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
