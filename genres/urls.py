from django.urls import path
from genres.views import genres_view

urlpatterns = [
    path('genres/', genres_view, name='genres'),
]
