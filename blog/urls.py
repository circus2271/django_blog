from django.conf.urls import url
from blog.views import PostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list_view'),
]
