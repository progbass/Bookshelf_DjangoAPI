from rest_framework import serializers

from .models import Book
from modules.Authors.serializers import AuthorSerializer

# Create your models here.
GENEROS = (
    ("CS", "Ciencia Ficción"),
    ("FS", "Fantasia"),
    ("TR", "Terror"),
    ("IT", "Tecnología"),
    ("DR", "Drama")
)


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    class Meta:
            model = Book
            fields = '__all__'
            #exclude = ('is_alive',)


class QueryBookSerializer(serializers.Serializer):
    date_published = serializers.DateField(required=False)
    literary_genre = serializers.ChoiceField(choices=GENEROS,required=False)
    raiting = serializers.DecimalField(max_digits=3,decimal_places=2, required=False)
    #raiting_lte = serializers.DecimalField(max_digits=3,decimal_places=2, required=False)
    

