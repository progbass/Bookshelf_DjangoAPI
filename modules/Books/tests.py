from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from ..Authors.models import Author

import datetime as dt
import json


class BooksTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name='test',
            nacionalidad='MX',
            biography='asdasdasdasd',
            gender='M',
            age=45,
            is_alive=True
        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            prologue='asdasd asdasd',
            price='230.00',
            cover='http://image.jpg'
        )
    
    def test_get_all_books(self):
    	#response = self.client.get('/books/{}'.format(self.book1.id))
    	response = self.client.get(reverse('books:list_books'))
    	books = Book.objects.all()
    	serializer = BookSerializer(books, many=True)
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(serializer.data, response.data)

    def test_get_book(self):
    	response = self.client.get('/api/v1/books/{}/'.format(self.book1.id))
    	book = Book.objects.get(pk=self.book1.id)
    	serializer = BookSerializer(book, many=True)
    	self.assertEqual(response.status_code, 200)
    	#self.assertEqual(serializer.data, response.data)
    
    def test_delete_book(self):
    	response = self.client.delete('/api/v1/books/{}/'.format(self.book1.id))
    	self.assertEqual(response.status_code, 204)

    #@classmethod
    #def setUpTestData(cls):
    	#Pass


