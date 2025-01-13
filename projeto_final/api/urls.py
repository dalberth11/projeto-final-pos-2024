from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, ToDoViewSet
from django.conf import settings
from django.conf.urls.static import static

# Definir o roteador e registrar os ViewSets
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)
router.register('todos', ToDoViewSet)

# Adicionar as rotas do roteador ao urlpatterns
urlpatterns = router.urls

# Adicionar a configuração para servir arquivos estáticos durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
