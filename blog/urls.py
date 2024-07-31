from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home_page'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blogs/create', BlogCreateView.as_view(), name='post_create'),
]
