from django.contrib import admin

from .models import Movie, Genre

class GenreInline(admin.StackedInline):
	model = Genre
	extra = 2

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
		('Other Information', {'fields': ['top99popularity', 'director', 'imdb_score']}),
	]

	inlines = [GenreInline]

admin.site.register(Movie, MovieAdmin)
