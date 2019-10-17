from django.shortcuts import render
from blog.models import  Post


def index(request):
  elPost=Post.objects.get(id=1)
  return render(request, 'paginaA.html', {'post' : elPost})
