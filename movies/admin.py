from django.contrib import admin
from .models import Actor, Director, Movie, Genre

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_of_birth')
    

@admin.register(Genre)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_feilds = ('name',)





@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_of_birth')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating', 'director')
    filter_horizontal = ('actors', 'genre')  # Handles many-to-many fields in admin
    list_filter = ('director', 'release_date')
