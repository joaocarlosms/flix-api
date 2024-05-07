from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genres_detail'),
]
