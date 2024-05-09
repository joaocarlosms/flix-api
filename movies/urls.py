from django.urls import path
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroy

urlpatterns = [
    path(
        'movies/', 
        MovieListCreateView.as_view(),
        name='movies-list-create'
    ),
    path(
        'movies/<int:pk>/',
        MovieRetrieveUpdateDestroy.as_view(),
        name='movies-details'
    )
]
