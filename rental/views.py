from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def index(request):
    all_movies = Movie.objects.all() #read the movie table to a list
    return render(request, 'index.html', { 'title': 'Movie Catalog', 'movies': all_movies })

def about(request):
    return HttpResponse("I'm Dru!!")

def soon(request):
    return render(request,"soon.html")

def catalog(request):
    return render(request, 'catalog.html')

def details(request, movie_id):
    try:
        the_movie = Movie.objects.get(id = movie_id)
        return render(request, 'details.html', { 'test' : 'It works!', 'movie' : the_movie})
    except:
        return render(request, 'NotFound.html')