from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.viewsets import ModelViewSet
from .models import User, ToDo, Post, Comment, Album, Photo 
from .serializers import UserSerializer, PostSerializer, CommentSerializer, AlbumSerializer, PhotoSerializer, ToDoSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

def home(request):
    return render(request, 'index.html')


# Simulando um banco de dados em memória para usuários
USERS = []

def index(request):
    """Renderiza a página principal."""
    return render(request, 'api/index.html')

@csrf_exempt
def api_users(request):
    """API para manipular os usuários."""
    if request.method == 'GET':
        return JsonResponse(USERS, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return JsonResponse({'error': 'Nome e email são obrigatórios'}, status=400)

        USERS.append({'name': name, 'email': email})
        return JsonResponse({'message': 'Usuário criado com sucesso'}, status=201)

    return JsonResponse({'error': 'Método não permitido'}, status=405)



