from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # Examples:
    # url(r'^$', 'goodreads.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/authors/', include('modules.Authors.urls')),
    url(r'^api/v1/books/', include('modules.Books.urls')), 
    url(r'^api/v1/users/', include('modules.Users.urls')),     
    #url(r'^api/v1/auth/$', obtain_jwt_token),     
    #url(r'^api/v1/auth/refresh/$', refresh_jwt_token),
    #url(r'^api/v1/auth/verify/$', verify_jwt_token),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]