from django.contrib import admin

# Registrando os modelos no painel admin do django

from .models import Post

admin.site.register(Post)