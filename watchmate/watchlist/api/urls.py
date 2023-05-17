from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import MovieListAV, MovieDetailAV
import watchlist

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-details'),
]