from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category, Tag
import markdown2
import time
from datetime import datetime, date

# Create your views here.
def ArticleAdd(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'control/article/add.html', context)


def ArticleAddHandler(request):
    if request.method == 'POST':
        article = Article()
        article.id = int(time.mktime(datetime.now().timetuple()))
        article.title = request.POST.get('title', '')
        article.body = request.POST.get('body', '')
        article.category = Category.objects.get(id=int(request.POST.get('category')))
        article.save()

    return HttpResponseRedirect('/admin/article/add')


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