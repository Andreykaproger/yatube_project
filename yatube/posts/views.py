from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'это главная страница Yatube'
    context = {
        'title' : title,
        'text' : 'Это главная страница'
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        'filter' : slug,
        'text' : 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request,template, context)


