from django.contrib import admin
from django.urls import path, include
import genres
import actors
import movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genres.urls')),
    path('', include('actors.urls')),
    path('', include('movies.urls')),
]
