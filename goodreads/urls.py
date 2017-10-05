from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Examples:
    url(r'^$', 'modules.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/authors/', include('modules.Authors.urls')),
    url(r'^api/v1/books/', include('modules.Books.urls', namespace="books")), 
    url(r'^api/v1/users/', include('modules.Users.urls')),     
    #url(r'^api/v1/auth/$', obtain_jwt_token),     
    #url(r'^api/v1/auth/refresh/$', refresh_jwt_token),
    #url(r'^api/v1/auth/verify/$', verify_jwt_token),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', include_docs_urls(title='Goodreads API')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


