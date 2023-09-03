from rest_framework.authtoken import views as Views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', Views.obtain_auth_token, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
