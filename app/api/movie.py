from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Movie
from app.serializers import MovieSerializer, GenreCreateSerializer
from rest_framework.permissions import IsAdminUser

class MovieCreate(APIView):

	"""
		Api to create movie
	"""	

	# Can be accessed by admin only
	permission_classes = (IsAdminUser,)

	def post(self, request, format=None):

		genres = request.data["genres"]

		serializer = MovieSerializer(data=request.data)
		created_genres = []

		# check if the data is validated by serializer
		if serializer.is_valid():
			serializer.save()

			for genre in genres:
				data = {'name':genre, 'movie': serializer.data['id']}
				# validation data across Genre serializer
				gen_serializer = GenreCreateSerializer(data=data)

				if gen_serializer.is_valid():
					gen_serializer.save()
					created_genres.append(gen_serializer.data)

			return Response({'movie': serializer.data, 'genres': created_genres}, status=status.HTTP_201_CREATED)

			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieHandler(APIView):

	"""
		Api to edit and delete movie objects
	"""

	# Can be accessed by admin only
	permission_classes = (IsAdminUser,)

	def put(self, request, id, format=None):

		try:
			movie = Movie.objects.get(id=id)
		except Movie.DoesNotExist:
			return Response("No data exist with id=%s"%str(id))

		serializer = MovieSerializer(movie, data=request.data)

		# check if the data is validated by serializer
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):

		try:
			movie = Movie.objects.get(id=id)
		except Movie.DoesNotExist:
			return Response("No data exist with id=%s"%str(id))

		movie.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
