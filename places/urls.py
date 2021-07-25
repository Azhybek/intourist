from  django.urls import path
from .views import places, create_place, place, delete_place, edit_place, FeedbackView, FeedbackDetailView

urlpatterns = [
    path('', places, name='places_list'),
    path('create/', create_place, name='create_place'),
    path('<int:id>/', place, name='place'),
    path('<int:id>/edit/', edit_place, name='edit_place'),
    path('<int:id>/delete/', delete_place, name='delete_place'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]