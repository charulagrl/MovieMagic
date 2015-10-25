from django.db import models


class Movie(models.Model):

	name = models.CharField(max_length=100)
	top99popularity = models.FloatField(default=0)
	director = models.CharField(max_length=100)
	imdb_score = models.FloatField(default=0)


class Genre(models.Model):

	name = models.CharField(max_length=100)
	movie = models.ForeignKey('Movie', null=True, blank=True)

