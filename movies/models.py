from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Director(models.Model):

    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    poster = models.ImageField(upload_to="movie_posters/",blank=True, null=True)


    def __str__(self):
        return self.title
    


