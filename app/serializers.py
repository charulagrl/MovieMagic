from rest_framework import serializers
from models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('name', 'top99popularity', 'director', 'imdb_score', 'id')

class GenreCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('name', 'id', 'movie')
        
class GenreDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('name', )
