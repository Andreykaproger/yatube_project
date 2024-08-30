from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)

    # template = 'posts/index.html'
    # title = 'это главная страница Yatube'
    # context = {
    #     'title': title,
    #     'text': 'Это главная страница'
    # }
    # return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug = slug)
    posts = Post.objects.filter(group = group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    # template = 'posts/group_list.html'
    # context = {
    #     'filter': slug,
    #     'text': 'Здесь будет информация о группах проекта Yatube'
    # }
    return render(request, 'posts/group_list.html', context)


