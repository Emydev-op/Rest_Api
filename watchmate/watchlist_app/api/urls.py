from django.urls import path
from . import views

# urlpatterns = [
#     path('list/', views.movie_list, name="movie-list"),
#     path('<int:pk>/', views.movie_details, name="movie-detail"),
# ]

urlpatterns = [
    path('list/', views.WatchListAView.as_view(), name="watch-list"),
    path('list/<int:pk>/', views.WatchDetailAV.as_view(), name="watch-detail"),
    path('stream/', views.StreamPlatformAV.as_view(), name="platform-list"),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name="platform-detail"),
]
