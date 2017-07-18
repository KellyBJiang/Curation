from django.conf.urls import url, include 
from django.views.generic import ListView, DetailView
from administrator.models import Post, User

urlpatterns = [
        url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("id")[:25], template_name="administrator/administrator.html")),
        url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'administrator/post.html')),
        url(r'^$', ListView.as_view(queryset = User.objects.all().order_by("id")[:25], template_name="administrator/assign.html")),
        url(r'^(?P<pk>\d+)$', DetailView.as_view(model = User, template_name = 'administrator/datadetail.html'))
    ] ##decending order , add -, only show the latest 25n file