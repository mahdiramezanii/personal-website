from django.shortcuts import render
from .models import Article,Tag
from django.views.generic import ListView,View,DetailView

class ArticleView(ListView):

    model = Article
    template_name = "Blog_app/blog.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "Blog_app/blog-post.html"
