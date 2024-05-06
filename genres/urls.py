from django.urls import path
from genres.views import GenreCreateListView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'),
    # path('genres/<int:pk>/', genre_detail_view, name='genres_detail'),
]
