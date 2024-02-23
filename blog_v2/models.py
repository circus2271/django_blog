from django.db import models

# Article model
# Tag model
# Author model

class Author(models.Model):
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	# TODO: validate username so it only starts with @
	username = models.CharField(max_length=30, primary_key=True)
	author_info = models.TextField(max_length=700, null=True)
	# email

	def published_articles(self):
		published_articles = self.article_set.filter(published=True)
		return published_articles

	def drafts(self):
		drafts = self.article_set.filter(published=False)
		return drafts

	def __str__(self):
		return self.username


class Article(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField(max_length=145)
	main_text = models.TextField(max_length=2000)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	# TODO: set published_date only after actual publishment
	published_date = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True, editable=False)
	published = models.BooleanField(default=False)
	# TODO: add current views number
	hero_image = models.ImageField(upload_to='hero_images')

	class Meta:
		ordering = ['-published_date']

	def __str__(self):
		return self.title


class Tag(models.Model):
	slug = models.CharField(max_length=24, unique=True)
	articles = models.ManyToManyField(Article)

	def published_articles(self):
		published_articles = self.articles.filter(published=True)
		return published_articles

	def drafts(self):
		drafts = self.articles.filter(published=False)
		return drafts

	def __str__(self):
		return self.slug
