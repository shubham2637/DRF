from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist.api.permissions import AdminOrReadOnly


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
#
#
# class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create( request, *args, **kwargs )
#
#
# class StreamPlatformView(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, context={'request': request})
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformView(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [AdminOrReadOnly]

    def perform_create(self, serializer):
        watchlist_id = self.kwargs.get('watchlist_id')
        review_user_id = self.request.user.pk
        review_queryset = Review.objects.filter( watchlist_id=watchlist_id, review_user_id=review_user_id )
        if review_queryset.exists():
            raise ValidationError(f"{self.request.user.username} has already submitted a Review")
        serializer.save(watchlist_id=watchlist_id, review_user_id=review_user_id)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()  # now using get_queryset for custom queryset
    serializer_class = ReviewSerializer
    permission_classes = [AdminOrReadOnly]

    def get_queryset(self):
        watchlist_id = self.kwargs['watchlist_id']
        return Review.objects.filter(watchlist=watchlist_id)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AdminOrReadOnly]


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
        serializer = StreamPlatformSerializer( stream_platforms, many=True, context={'request': request})
        return Response( serializer.data, status=status.HTTP_200_OK )

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class StreamPlatformDetailAV( APIView ):

    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get( pk=pk )
            stream_platform_serializer = StreamPlatformSerializer( stream_platform, context={'request': request})
            return Response( stream_platform_serializer.data, status=status.HTTP_200_OK )
        except ObjectDoesNotExist:
            return Response( {"error": "Stream Platform invalid id"}, status=status.HTTP_404_NOT_FOUND )

    def put(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get( pk=pk )
            stream_platform_serializer = StreamPlatformSerializer( stream_platform, data=request.data,
                                                                   context={'request' : request})
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
