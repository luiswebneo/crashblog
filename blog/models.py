from django.db import models

# Criando os modelos de banco de dados do app

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ('created_at',)