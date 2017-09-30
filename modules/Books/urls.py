from django.conf.urls import include, url
from django.contrib import admin
#from .views import ListBook,DetailBook
from .generic_view import ListBook, DetailBook, UpdateBookCover

urlpatterns = [
    url(r'^$', ListBook.as_view(), name="list_books"),
    url(r'^(?P<pk>[0-9]+)/$', DetailBook.as_view(), name="detail_book"),
    url(r'^cover/$', UpdateBookCover.as_view())
]
