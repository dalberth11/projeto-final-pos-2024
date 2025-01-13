from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, ToDoViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)
router.register('todos', ToDoViewSet)

urlpatterns = router.urls