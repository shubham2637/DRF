from django.urls import path
from watchlist.views import movie_list, movie_details

import watchlist

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:movie_id>/', movie_details, name='movie-details'),
]