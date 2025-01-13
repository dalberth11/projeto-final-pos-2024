from django.shortcuts import render, get_object_or_404, redirect
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
        # Retorna todos os usuários do banco de dados
        users = User.objects.all()
        users_data = [{'name': user.name, 'email': user.email} for user in users]
        return JsonResponse(users_data, safe=False)

    if request.method == 'POST':
        # Criação de um novo usuário no banco de dados
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return JsonResponse({'error': 'Nome e email são obrigatórios'}, status=400)

        user = User.objects.create(name=name, email=email)
        return JsonResponse({'message': 'Usuário criado com sucesso'}, status=201)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

def usuarios(request):
    """Exibe a página com a lista de usuários."""
    users = User.objects.all()  # Pega todos os usuários do banco de dados
    return render(request, 'api/usuarios.html', {'users': users})  # Passa os usuários para o template

def listar_usuarios(request):
    users = User.objects.all()  # Pega todos os usuários do banco de dados
    return render(request, 'usuarios.html', {'users': users})

def editar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('listar_usuarios')  # Redireciona para a lista de usuários
    
    return render(request, 'editar_usuario.html', {'user': user})

def excluir_usuario(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('listar_usuarios')  # Redireciona para a lista de usuários
    
    return render(request, 'confirmar_exclusao.html', {'user': user})

def criar_usuario(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Cria o novo usuário e salva no banco de dados
        user = User(name=name, email=email)
        user.save()

        # Redireciona para a página de lista de usuários
        return redirect('usuarios')  # Substitua 'usuarios' pela sua URL de lista de usuários

    return render(request, 'criar_usuario.html')  # Retorna o formulário vazio para GET