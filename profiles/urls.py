from django.urls import path
from . import views # . all

urlpatterns = [
    path('profile/', views.UserProfilePrivateView.as_view()), # for user view
    path('profile/<int:pk>/', views.UserProfilePublicView.as_view({'get': 'retrieve'})), # for other users view
]
