from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('news', views.PostListNews.as_view(), name='news'),
    path('tips&lifestyle', views.PostListTips.as_view(), name='tips'),
    path('diyprojects', views.PostListDiy.as_view(), name='diy'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
