from .base import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DBNAME',''),
        'USER': os.getenv('DBUSER',''),
        'PASSWORD': os.getenv('DBPASSWORD',''),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# SESSION_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https://')
STATIC_ROOT = os.path.join(os.getcwd(), 'static')

