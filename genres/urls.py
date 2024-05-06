from django.urls import path
from genres.views import genre_detail_view, genres_create_list_view

urlpatterns = [
    path('genres/', genres_create_list_view, name='genres'),
    path('genres/<int:pk>/', genre_detail_view, name='genres_detail'),
]
