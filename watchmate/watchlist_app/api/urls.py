from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# urlpatterns = [
#     path('list/', views.movie_list, name="movie-list"),
#     path('<int:pk>/', views.movie_details, name="movie-detail"),
# ]
router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAView.as_view(), name="watch-list"),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name="watch-detail"),
    # path('stream/', views.StreamPlatformAV.as_view(), name="platform-list"),
    # path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name="platform-detail"),
    path('', include(router.urls)),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name="review-detail"),
    
    path('reviews/', views.UserReview.as_view(), name="user-review-details"),
    # path('review/', views.ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name="review-detail"),    
]