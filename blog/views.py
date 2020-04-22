from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostListNews(generic.ListView):
    queryset = Post.objects.filter(
        Q(section=0) & Q(status=1)).order_by('-created_on')
    template_name = 'news.html'


class PostListTips(generic.ListView):
    queryset = Post.objects.filter(
        Q(section=1) & Q(status=1)).order_by('-created_on')
    template_name = 'tips.html'


class PostListDiy(generic.ListView):
    queryset = Post.objects.filter(
        Q(section=2) & Q(status=1)).order_by('-created_on')
    template_name = 'diy.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
