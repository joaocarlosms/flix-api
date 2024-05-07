from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path(
        'actors/', 
        ActorCreateListView.as_view(), 
        name='actors-create-list'
    ),
    path(
        'actors/<int:pk>/', 
        ActorRetrieveUpdateDestroyView.as_view(),
        name='actors-detail'
    ),
]