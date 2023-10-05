from django.urls import path
# from django.views.generic.base import RedirectView
# from blog.views import ArticleListView, ArticleDetailView, AuthorListView, AuthorDetailView, AuthorDraftDetailView, TagListView, TagDetailView
from . import views

app_name='image_uploader'
urlpatterns = [
#     path('test/', views.test, name='test'),
    path('', views.test, name='test'),
]
