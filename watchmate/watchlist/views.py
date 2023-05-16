from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from watchlist.models import Movie
from django.http import JsonResponse


# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list( movies.values() )
    }
    return JsonResponse( data )


def movie_details(request, movie_id):
    data = dict()
    try:
        movie = Movie.objects.get( pk=movie_id )
        data['name'] = movie.name
        data['description'] = movie.description
        data['active'] = movie.active
    except ObjectDoesNotExist:
        data['error'] = "Invalid Movie id"
    return JsonResponse(data)

