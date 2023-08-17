from django.urls import path
from . import views

# urlpatterns = [
#     path('list/', views.movie_list, name="movie-list"),
#     path('<int:pk>/', views.movie_details, name="movie-detail"),
# ]

urlpatterns = [
    path('list/', views.MovieListAView.as_view(), name="movie-list"),
    path('<int:pk>/', views.MovieDetailAV.as_view(), name="movie-detail"),
]
