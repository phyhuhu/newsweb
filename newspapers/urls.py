from django.urls import path
# from .views import ArticlesListView
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.news_home, name='news-home'),

    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]

