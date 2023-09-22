from django.urls import path
from django.views.generic.base import RedirectView
from blog.views import ArticleListView, ArticleDetailView, AuthorListView, AuthorDetailView, TagListView, TagDetailView
from . import views

app_name='blog'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('', RedirectView.as_view(pattern_name='blog:articles'), name='home_page'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<str:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/<slug>', TagDetailView.as_view()),
]