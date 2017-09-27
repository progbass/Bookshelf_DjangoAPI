#Cosas de Django
from django.shortcuts import render
from django.http import Http404
#Cosas de DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#Son mis cosas
from .serializers import BookSerializer,QueryBookSerializer
from .models import Book
from django.db.models import Q

class ListBook(APIView):

    def get(self, request):
        if request.query_params:
            queryparam = QueryBookSerializer(data=request.query_params)
            if queryparam.is_valid():                
                data = queryparam.validated_data
                books = []
                if data.get('raiting',None):
                    books.append(Book.objects.filter(
                        raiting=data.get('raiting',5.0)
                        ))
                elif data.get('raiting_lte',None):
                    books.append(Book.objects.filter(
                        raiting__lte=data.get('raiting_lte',5.0)                    
                        ))                                
                serializer = BookSerializer(books,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(queryparam.errors, status=status.HTTP_400_BAD_REQUEST)        
        else:
            Books = Book.objects.all() #querysets SELECT * FROM Book
            serializer  = BookSerializer(Books,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailBook(APIView):

    def _getBook(self,pk):
        try:
            book = Book.objects.get(pk=pk)
            return book
        except Book.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        Book = self._getBook(pk)
        serializer = BookSerializer(Book)        
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self,request,pk):
        Book = self._getBook(pk)
        serializer = BookSerializer(Book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk):
        serializer =  self._getBook(pk)
        #serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk):
        Book = self._getBook(pk)
        serializer = BookSerializer(Book,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    