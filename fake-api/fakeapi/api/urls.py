from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ToDoViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', ToDoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
