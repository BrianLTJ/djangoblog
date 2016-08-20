from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category, Tag
import markdown2
import time
from datetime import datetime, date

# Create your views here.
def GetIDBasedOnTime():
    return int(time.mktime(datetime.now().timetuple()))


def Index(request):
    return render(request, 'control/base.html')


def ArticleAdd(request):
    category = Category.objects.all()
    context = {'category': category, 'pageattr': 'n'}
    return render(request, 'control/article/add.html', context)


def ArticleAddHandler(request):
    if request.method == 'POST':
        article = Article()
        article.id = GetIDBasedOnTime()
        article.title = request.POST.get('title', ' ')
        article.abstract = request.POST.get('abstract', ' ')
        article.body = request.POST.get('body', ' ')
        article.category = Category.objects.get(id=int(request.POST.get('category')))
        article.save()

    return HttpResponseRedirect()


def ArticleEditHandler(request):
    if request.method == 'POST':
        article = Article.objects.get(id=request.POST.get('id'))
        article.title = request.POST.get('title', ' ')
        article.abstract = request.POST.get('abstract', ' ')
        article.body = request.POST.get('body', ' ')
        article.category = Category.objects.get(id=int(request.POST.get('category')))

    return HttpResponseRedirect(url())


def ArticleList(request, page_type):
    if page_type == 'all':
        article_list = Article.objects.all()
    elif page_type == 'draft':
        article_list = Article.objects.filter(status='d')
    elif page_type == 'published':
        article_list = Article.objects.filter(status='p')
    elif page_type == 'recycle':
        article_list = Article.objects.filter(status='r')
    else:
        return Http404

    context = {'article_list': article_list, 'list_type': page_type[0:1]}
    return render(request, 'control/article/list.html', context)


class ArticleEdit(DetailView):
    model = Article
    template_name = "control/article/edit.html"
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleEdit, self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj


class CategoryList(ListView):
    model = Category
    template_name = 'control/attr/category.html'

    def get_queryset(self):
        category_list = Category.objects.all()
        return category_list


def CategoryAddHandler(request):
    if request.method == 'POST':
        cate = Category()
        # cate.id = GetIDBasedOnTime()
        cate.name = request.POST.get('new_cate', ' ')
        cate.save()

    return HttpResponseRedirect('/admin/attr/category')


def CategoryEditHandler(request):
    if request.method == 'POST':
        cate = Category.objects.get(id=request.POST.get('id'))
        cate.name = request.POST.get('name')
        cate.save()
    return HttpResponseRedirect('/admin/attr/category')


def CategoryDelHandler(request):
    if request.method == 'POST':
        Category.objects.get(id=request.POST.get('id')).delete()
    return HttpResponseRedirect('/admin/attr/category')


class TagList(ListView):
    model = Tag
    template_name = 'control/attr/tag.html'

    def get_queryset(self):
        tag_list = Tag.objects.all()
        return tag_list


def TagAddHandler(request):
    if request.method == 'POST':
        tag = Tag()
        # tag.id = GetIDBasedOnTime()
        tag.name = request.POST.get('new_tag', ' ')
        tag.save()

    return HttpResponseRedirect('/admin/attr/tag')


def TagEditHandler(request):
    if request.method == 'POST':
        tag = Tag.objects.get(id=request.POST.get('id'))
        tag.name = request.POST.get('name')
        tag.save()
    return HttpResponseRedirect('/admin/attr/tag')


def TagDelHandler(request):
    if request.method == 'POST':
        Tag.objects.get(id=request.POST.get('id')).delete()
    return HttpResponseRedirect('/admin/attr/Tag')



