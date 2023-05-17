from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from watchlist.models import WatchList, StreamPlatform
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer


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


class WatchListAV( APIView ):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer( movies, many=True )
        return Response( serializer.data )

    def post(self, request):
        serializer = WatchListSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class WatchListDetailAV( APIView ):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get( pk=pk )
            serializer = WatchListSerializer( movie )
            return Response( serializer.data, status=status.HTTP_200_OK )
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get( pk=pk )
            serializer = WatchListSerializer( movie, data=request.data )
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data, status=status.HTTP_201_CREATED )
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get( pk=pk )
            movie.delete()
            return Response( status=status.HTTP_204_NO_CONTENT )
        except ObjectDoesNotExist:
            data = {"error": "Invalid Movie id"}
            return Response( data, status=status.HTTP_404_NOT_FOUND )


class StreamPlatformListAV( APIView ):

    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer( stream_platforms, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class StreamPlatformDetailAV( APIView ):

    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get( pk=pk )
            stream_platform_serializer = StreamPlatformSerializer( stream_platform )
            return Response( stream_platform_serializer.data, status=status.HTTP_200_OK )
        except ObjectDoesNotExist:
            return Response( {"error": "Stream Platform invalid id"}, status=status.HTTP_404_NOT_FOUND )

    def put(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get( pk=pk )
            stream_platform_serializer = StreamPlatformSerializer( stream_platform, data=request.data )
            if stream_platform_serializer.is_valid():
                stream_platform_serializer.save()
                return Response( stream_platform_serializer.data, status=status.HTTP_202_ACCEPTED )
            return Response( stream_platform_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        except ObjectDoesNotExist:
            return Response( {"error": "Stream Platform invalid id"}, status=status.HTTP_404_NOT_FOUND )

    def delete(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get( pk=pk )
            stream_platform.delete()
            return Response( {"res_str": "Deletion Successful"}, status=status.HTTP_204_NO_CONTENT )
        except ObjectDoesNotExist:
            return Response( {"error": "Stream Platform invalid id"}, status=status.HTTP_404_NOT_FOUND )
