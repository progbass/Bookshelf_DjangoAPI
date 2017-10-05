"""
WSGI config for goodreads project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
import os
#from whitenoise.django import DjangoWhiteNoise	

try:
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path)
except:
    pass


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goodreads.settings.production")
application = get_wsgi_application()
# application = DjangoWhiteNoise(application)

