from django.urls import include, path
from core.views import AuthViewSet, BlogPostListCreateView, BlogPostDetailView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
]