from django.urls import path
from . import views # . all

urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view({'get': 'retrieve', 'put': 'update'})), # for user view
    path('<int:pk>/', views.UserProfilePublicView.as_view({'get': 'retrieve'})), # for other users view
]
