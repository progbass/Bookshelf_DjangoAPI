#Son mis cosas
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings

from .serializers import BookSerializer
from .models import Book

import uuid
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope




class UpdateBookCover(APIView):
	parser_classes = (FormParser, MultiPartParser)

	def post(self, request):
		try:
			FileUploadHandler().handle_uploaded_file(request.FILES['file'])
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status=status.HTTP_200_OK)



class FileUploadHandler():
	def handle_uploaded_file(self, f):
		extension = str(f).split(".")[-1]
		filename = "{}.{}".format(uuid.uuid4(), extension)
		path = "%s/%s" % (settings.MEDIA_ROOT, filename)
		with open(path, 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)

		return filename


class ListBook(generics.ListCreateAPIView): # GET y POST
	parser_classes = (FormParser, MultiPartParser)
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	filter_backends = (filters.SearchFilter,DjangoFilterBackend)
	filter_fields = ('raiting', 'date_published', 'price', 'literary_genre')
	search_fields = ('title', 'prologue', 'literary_genre')
	permission_classes = (IsAuthenticated, TokenHasReadWriteScope)

	def create(self, request):
		try:
			filename = FileUploadHandler().handle_uploaded_file(request.FILES['file'])
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		request.data['cover'] = request.build_absolute_uri(settings.MEDIA_URL) + filename
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBook(generics.RetrieveUpdateDestroyAPIView):# GET,PUT,DELETE,PATCH
	permission_classes = (IsAuthenticated, TokenHasScope)
	required_scopes = ['write']
	serializer_class = BookSerializer
	queryset = Book.objects.all() 





