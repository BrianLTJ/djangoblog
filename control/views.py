from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category, Tag
import markdown2

# Create your views here.
class ArticleAll(ListView):
    template_name = 'control/article/all.html'
    model = Article

    def get_queryset(self):
        article_list = Article.objects.all()
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

class ArticlePublished(ListView):
    template_name = 'control/article/published.html'
    model = Article

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list


class ArticleDraft(ListView):
    template_name = 'control/article/draft.html'
    model = Article

    def get_queryset(self):
        article_list = Article.objects.filter(status='d')
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list


class ArticleRecycle(ListView):
    template_name = 'control/article/recycle.html'
    model = Article

    def get_queryset(self):
        article_list = Article.objects.filter(status='r')
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list


class ArticleEdit(DetailView):
    model = Article
    template_name = "control/article/edit.html"
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleEdit, self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj