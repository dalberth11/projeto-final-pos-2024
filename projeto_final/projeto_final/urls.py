"""
URL configuration for projeto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import home
from api import views

router = DefaultRouter()


urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('api/users/', views.api_users, name='api_users'),  # Endpoint para manipulação de usuários
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
]
