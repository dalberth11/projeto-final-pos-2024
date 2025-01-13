from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=200)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=200)
    url = models.URLField()
    thumbnail_url = models.URLField()
