from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from app.serializers import MovieSerializer, GenreDisplaySerializer
from app.models import Movie, Genre
from app import search_util

class MoviesList(APIView):
    """
        List all the movies
    """

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class MovieList(APIView):
    """
        Get movie by its id
    """
    def get(self, request, id):

        try:
            movie = Movie.objects.get(id=id)
            genres = Genre.objects.filter(movie=id)

        except Movie.DoesNotExist:
            return Response("No data exist with id=%s"%str(id))

        if request.method == 'GET':
            movie_serializer = MovieSerializer(movie)
            genre_serializer = GenreDisplaySerializer(genres, many=True)

            return Response({
                'movie_data': movie_serializer.data,
                'genres': genre_serializer.data 
            })


class SearchMovie(APIView):
    """
        Api to search for movie by its name or director
    """
    def get(self, request):

        query_string = ''
        found_entries = None

        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = search_util.get_query(query_string)
        
        found_entries = Movie.objects.filter(entry_query)
        serializer = MovieSerializer(found_entries, many=True)

        return Response(serializer.data)
