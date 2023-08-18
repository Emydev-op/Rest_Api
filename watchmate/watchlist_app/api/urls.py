from django.urls import path
from . import views

# urlpatterns = [
#     path('list/', views.movie_list, name="movie-list"),
#     path('<int:pk>/', views.movie_details, name="movie-detail"),
# ]

urlpatterns = [
    path('list/', views.WatchListAView.as_view(), name="movie-list"),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name="movie-detail"),
    path('stream/', views.StreamPlatformAV.as_view(), name="stream-serializer"),
]
