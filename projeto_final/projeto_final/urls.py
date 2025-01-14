from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)
router.register('albums', views.AlbumViewSet)
router.register('photos', views.PhotoViewSet)
router.register('todos', views.ToDoViewSet)

urlpatterns = [
    path('', lambda request: redirect('/api/users/')),  # Redireciona para /api/users/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Usa o DefaultRouter para as rotas da API
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
]
