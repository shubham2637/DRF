from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, \
    ReviewList, ReviewDetail, ReviewCreate
import watchlist

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-details'),

    path('stream/list/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),

    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
]