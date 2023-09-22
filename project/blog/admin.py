from django.contrib import admin
from blog.models import Article, Author, Tag

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Author)
