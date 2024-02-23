from django.contrib import admin
from blog_v2.models import Article, Author, Tag

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Author)
