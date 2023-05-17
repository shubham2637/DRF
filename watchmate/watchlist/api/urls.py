from django.urls import path
from watchlist.api.views import movie_list, movie_detail

import watchlist

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:movie_id>/', movie_detail, name='movie-details'),
]