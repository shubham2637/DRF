from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get( pk=movie_id )

    except ObjectDoesNotExist:
        data = {"error": "Invalid Movie id"}
        return Response( data )

    if request.method == 'GET':
        serializer = MovieSerializer( movie )
        return Response( serializer.data )

    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        else:
            return Response( serializer.errors )



