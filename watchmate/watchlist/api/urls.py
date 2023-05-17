from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV
import watchlist

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-details'),
    path('platform/list/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]