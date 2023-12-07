from django.urls import path
from django.views.generic.base import RedirectView
#from blog.views import ArticleListView, ArticleDetailView, AuthorListView, AuthorDetailView, DraftListView, AuthorDraftDetailView, TagListView, TagDetailView
from . import views

app_name='outcinema'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.index, name='homepage'),
    path('films/', views.films, name='films'),
    path('films/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('events/', views.events, name='events'),
    path('rent/', views.rent, name='rent'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    #path('', RedirectView.as_view(pattern_name='blog:articles'), name='home_page'),
]
