from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    # Add this line for the root URL
     path('', views.home, name='home'), 
     path('movie/',views.movie_page,name='movie-page'),
     path('admin/', admin.site.urls),
     path('login/', views.user_login, name='login'),
     path('register/', views.user_signup, name='register'),
     path('logout/', views.logoutUser, name='logout'),
    # Add other URL patterns as needed
     path('movie_tickets/', views.movie_tickets_list, name='movie_tickets_list'),
    ]
