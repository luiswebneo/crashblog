from django.shortcuts import render

from blog.models import Post
###: 3 parte Criando as views do crashoblg.

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')
