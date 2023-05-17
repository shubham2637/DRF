from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, \
    ReviewList, ReviewDetail
import watchlist

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-details'),
    path('platform/list/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream_platform-details'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
]