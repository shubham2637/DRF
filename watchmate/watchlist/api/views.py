from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_detail(request, movie_id):
    data = dict()
    try:
        movie = Movie.objects.get( pk=movie_id )
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        data['error'] = "Invalid Movie id"
        return Response(data)
