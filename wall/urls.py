from django.urls import path
from . import views


urlpatterns = [
    path('comment/<int:pk>', views.CommentsView.as_view({'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('post/<int:pk>/', views.PostView.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/', views.PostListView.as_view())
]