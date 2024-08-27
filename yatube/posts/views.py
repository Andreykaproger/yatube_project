from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('главная страница')

def group_posts(request, slug):
    return HttpResponse(f'это страница с группами, отфильтрованными по {slug}')


