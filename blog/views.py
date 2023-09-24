from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from blog.models import Article, Author, Tag

def test(request):
	return JsonResponse(['wow', {'json': True}], safe=False)

class ArticleListView(ListView):
	# model = Article
	queryset = Article.objects.filter(published=True)
	context_object_name = 'articles'
	paginate_by = 4

	# def get_queryset(self):
    #    self.published = get_object_or_404(Publisher, name=self.kwargs["publisher"])
    #    return Book.objects.filter(publisher=self.publisher)

class ArticleDetailView(DetailView):
	# model = Article
	queryset = Article.objects.filter(published=True)
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
# 		context['author'] = Author.objects.all()
# 		context['author'] = Article.authors.all()
# 		print(context['author'])
		print('context', context)
		return context

class DraftArticleListView(LoginRequiredMixin, ListView):
	# model = Article
	queryset = Article.objects.filter(published=False)
	template_name = 'blog/drafts.html'
	context_object_name = 'drafts'
	paginate_by = 8
	# login_url = '/'
	redirect_field_name = None


	def get_login_url(self):
# 		return reverse('blog:authors')
		return reverse('admin:index')

class DraftArticleDetailView(LoginRequiredMixin, DetailView):
#	model = Article
	queryset = Article.objects.filter(published=False)

	template_name = 'blog/draft_detail.html'
	context_object_name = 'draft_detail'
	# login_url = '/'
	redirect_field_name = None

	def get_login_url(self):
# 		return reverse('blog:tags')
		return reverse('admin:index')

class AuthorListView(ListView):
	model = Author
	context_object_name= 'authors'
	# queryset = Author.objects.filter(article__published=True)

class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'author'
	#queryset = Author.objects.select_related('article_set')
	# queryset = Author.objects.filter(article__published=True)

	#def get_queryset(self):
	#	self.author = get_object_or_404(Author, pk=self.kwargs['pk'])
	#	return 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
#               context['author'] = Author.objects.all()
#               context['author'] = Article.authors.all()
		published_articles = context['author'].article_set.filter(published=True)
		print('pa', published_articles)
		context['published_articles'] = published_articles
		print(context)
		#print('qs', self.queryset)
		#for a in context['object'].article_set.all():
	#		print(a.published)
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
    		# Add in the publisher
    		print(context)
    		context['zhzh'] = 15
    		print(context)

    		return context
# #
# 	def get_queryset(self):
# 		slug = self.kwargs["slug"]
# 		print('slug ' + slug)
# 		return Tag.objects.get(name=slug)
