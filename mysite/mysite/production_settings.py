# mysite/mysite/production_settings.py

# Import all default settings.
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration.
import os.path

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join('static'), )

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = False