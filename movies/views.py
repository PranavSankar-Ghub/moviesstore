from django.shortcuts import render, get_object_or_404
from .models import Movie

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Actor, Genre, Director

def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_date = request.POST.get('release_date')
        rating = request.POST.get('rating')
        synopsis = request.POST.get('synopsis')
        poster = request.FILES.get('poster')
        director_id = request.POST.get('director')
        actor_ids = request.POST.getlist('actors')  # Handle many-to-many field
        genre_ids = request.POST.getlist('genre')  # Handle many-to-many field

        try:
            director = Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            return HttpResponse("Director not found", status=400)

        movie = Movie.objects.create(
            title=title,
            release_date=release_date,
            rating=rating,
            synopsis=synopsis,
            poster=poster,
            director=director
        )

        # Handle many-to-many relationships
        movie.actors.set(Actor.objects.filter(id__in=actor_ids))
        movie.genres.set(Genre.objects.filter(id__in=genre_ids))

        return redirect('movie_list')  # Redirect to a list of movies or wherever appropriate

    else:
        directors = Director.objects.all()
        actors = Actor.objects.all()
        genres = Genre.objects.all()
        return render(request, 'add_movie.html', {
            'directors': directors,
            'actors': actors,
            'genres': genres
        })

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movies_list(request):
    movies = Movie.objects.all()
    return render (request,'movies/movie_list.html',{ 'movies':movies})



