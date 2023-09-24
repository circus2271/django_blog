from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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


class AuthorListView(ListView):
	model = Author
	context_object_name= 'authors'


class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'author'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		published_articles = self.object.published_articles()
		drafts = self.object.drafts()
		context['published_articles'] = published_articles
		context['drafts'] = drafts

		return context


class AuthorDraftDetailView(LoginRequiredMixin, DetailView):
	model = Author
	template_name = 'blog/article_detail.html'
	context_object_name = 'article'

	def get_object(self, **kwargs):
		drafts = super().get_object().drafts()
		draft_detail = get_object_or_404(drafts, pk=self.kwargs['article_id'])

		return draft_detail

	def get_login_url(self):
		return reverse('admin:index')


class TagListView(ListView):
	model = Tag
	context_object_name = 'tags'


class TagDetailView(DetailView):
	model = Tag
	context_object_name = 'tag'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		published_articles = self.object.published_articles()
		print('pa', published_articles)
		context['published_articles'] = published_articles
		print(context)

		return context

