from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from blog.models import Article, Author, Tag

def test(request):
	return JsonResponse(['wow', {'json': True}], safe=False)

class ArticleListView(ListView):
	model = Article
	context_object_name = 'articles'
	paginate_by = 4

class ArticleDetailView(DetailView):
	model = Article
	context_object_name = 'article'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# # 		context['author'] = Author.objects.all()
# 		context['author'] = Article.authors.all()
# 		print(context['author'])
# 		return context

class AuthorListView(ListView):
	model = Author
	context_object_name= 'authors'

class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'author'

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
