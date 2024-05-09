from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path(
        'review/', 
        ReviewListCreateView.as_view(), 
        name='review-list-create'
    ),
    path(
        'reviews/<int:pk>/', 
        ReviewRetrieveUpdateDestroy.as_view(),
        name='review-details'
    )
]
