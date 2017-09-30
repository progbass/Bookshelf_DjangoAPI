from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oji_onyq4-^h10+ho9%7r7mf-6fv7q+!wrzp65co8)5w^)!!dh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'goodreads',
       'USER': 'progbass',
       'PASSWORD': 'inflames12',
       'HOST': 'localhost',
       'PORT': '5432'
   }
}

