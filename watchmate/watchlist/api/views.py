from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer

#
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, movie_id):
#     try:
#         movie = Movie.objects.get( pk=movie_id )
#
#     except ObjectDoesNotExist:
#         data = {"error": "Invalid Movie id"}
#         return Response( data , status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MovieSerializer( movie )
#         return Response( serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response( serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )



class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get( pk=pk)
            serializer = MovieSerializer( movie )
            return Response( serializer.data, status=status.HTTP_200_OK )
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get( pk=pk )
            movie.delete()
            return Response( status=status.HTTP_204_NO_CONTENT )
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )
