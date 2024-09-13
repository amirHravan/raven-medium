from django.urls import path

from .views import BlogListView, BlogCreateView, BlogUpdateDeleteView, BlogDetailView, BlogLikeView, BlogAnalyticsView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/', BlogUpdateDeleteView.as_view(), name='blog-update-delete'),
    path('<int:pk>/detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/like/', BlogLikeView.as_view(), name='blog-like'),
    path('analytics/', BlogAnalyticsView.as_view(), name='blog-analytics'),
]