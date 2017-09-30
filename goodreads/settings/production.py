from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oji_onyq4-^h10+ho9%7r7mf-6fv7q+!wrzp65co8)5w^)!!dh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allowed Hosts
ALLOWED_HOSTS = []

# Database
DATABASES = dict()
DATABASES['default'] = dj_databases_url.config() # <--- Heroku Only Configuration
SESSION_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https://')
STATIC_ROOT = os.path.join(os.getcwd(), 'static')


