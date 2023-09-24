from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from blog.models import Article, Author, Tag

def test(request):
	return JsonResponse(['wow', {'json': True}], safe=False)

class ArticleListView(ListView):
	queryset = Article.objects.filter(published=True)
	context_object_name = 'articles'
	paginate_by = 4

class ArticleDetailView(DetailView):
	queryset = Article.objects.filter(published=True)
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print('context', context)
		return context

class DraftArticleListView(LoginRequiredMixin, ListView):
	queryset = Article.objects.filter(published=False)
	template_name = 'blog/drafts.html'
	context_object_name = 'drafts'
	paginate_by = 8
	redirect_field_name = None

	def get_login_url(self):
		return reverse('admin:index')

class DraftArticleDetailView(LoginRequiredMixin, DetailView):
	queryset = Article.objects.filter(published=False)
	template_name = 'blog/draft_detail.html'
	context_object_name = 'draft_detail'
	redirect_field_name = None

	def get_login_url(self):
		return reverse('admin:index')

class AuthorListView(ListView):
	model = Author
	context_object_name= 'authors'

class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'author'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		published_articles = context['author'].article_set.filter(published=True)
		context['published_articles'] = published_articles

		return context

class TagListView(ListView):
	model = Tag
	context_object_name = 'tags'

class TagDetailView(DetailView):
	model = Tag
	context_object_name = 'tag'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		published_articles = context['tag'].articles.filter(published=True)
		print('pa', published_articles)
		context['published_articles'] = published_articles
		print(context)

		return context
