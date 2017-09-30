from .base import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']

# Database
DATABASES = dict()
DATABASES['default'] = dj_database_url.config() # <--- Heroku Only Configuration
SESSION_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https://')
STATIC_ROOT = os.path.join(os.getcwd(), 'static')

