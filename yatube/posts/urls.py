from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'start_page'),
    path('group/<slug:slug>/', views.group_posts, name = 'groups'),
]

