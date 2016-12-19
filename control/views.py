from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category, Tag
import markdown2
import time
from datetime import datetime, date

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def GetIDBasedOnTime():
    return int(time.mktime(datetime.now().timetuple()))


def login_index(request):

    return render(request, 'control/login/login.html')


def login_handler(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return HttpResponseRedirect('/admin')
        # else:
        #     return HttpResponseRedirect('/admin/login')
        return HttpResponseRedirect('/admin/login')
    else:
        return Http404


# @login_required(login_url='/admin/login')
def logout_handler(request):
    # logout(request)
    return HttpResponseRedirect('/admin')


# @login_required(login_url='/admin/login')
def Index(request):
    return render(request, 'control/index/index.html')


# @login_required(login_url='/admin/login')
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


# @login_required(login_url='/admin/login')
def ArticleAdd(request):
    category = Category.objects.all()
    tag = Tag.objects.all()
    context = {'category_list': category, 'pageattr': 'n', 'tag_list': tag}
    return render(request, 'control/article/content.html', context)


# @login_required(login_url='/admin/login')
def ArticleAddHandler(request):
    if request.method == 'POST':
        article = Article()
        article.id = GetIDBasedOnTime()
        article.title = request.POST.get('title', ' ')
        article.status = request.POST.get('status', 'd')
        article.abstract = request.POST.get('abstract', ' ')
        article.body = request.POST.get('body', ' ')
        article.category = Category.objects.get(id=int(request.POST.get('category')))
        article.save()
        tags = request.POST.getlist('tags[]')
        for tag in tags:
            article.tags.add(Tag.objects.get(id=tag))
        article.save()

    return HttpResponseRedirect('/admin/article/all')


class ArticleEdit(DetailView):
    login_url = '/admin/login'
    redirect_field_name = 'redirect_to'
    model = Article
    template_name = "control/article/content.html"
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleEdit, self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj

    def get_context_data(self, **kwargs):
        kwargs['pageattr'] = 'e'
        kwargs['category_list'] = Category.objects.all()
        kwargs['tag_list'] = Tag.objects.all()
        return super(ArticleEdit, self).get_context_data(**kwargs)


# @login_required(login_url='/admin/login')
def ArticleEditHandler(request):
    if request.method == 'POST':
        article = Article.objects.get(id=request.POST.get('id'))
        article.title = request.POST.get('title', ' ')
        article.abstract = request.POST.get('abstract', ' ')
        article.status = request.POST.get('status', 'd')
        article.body = request.POST.get('body', ' ')
        article.category = Category.objects.get(id=int(request.POST.get('category')))
        tags = request.POST.getlist('tags[]')
        article.tags.clear()
        for tag in tags:
            article.tags.add(Tag.objects.get(id=tag))
        article.save()

    return HttpResponseRedirect('/admin/article/all')


# @login_required(login_url='/admin/login')
def ArticleDelHandler(request, article_id):
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect('/admin/article/all')


# @login_required(login_url='/admin/login')
def ArticleRecycleHandler(request, article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'r'
    article.save()
    return HttpResponseRedirect('/admin/article/recycle')


# @login_required(login_url='/admin/login')
def ArticleRestoreToDraftHandler(request, article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'd'
    article.save()
    return HttpResponseRedirect('/admin/article/draft')


# @login_required(login_url='/admin/login')
def ArticlePublishHandler(request, article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'p'
    article.save()
    return HttpResponseRedirect('/admin/article/published')


# 文章置顶
# @login_required(login_url='/admin/login')
def ArticleTopHandler(request, article_id):
    article = Article.objects.get(id=article_id)
    article.topped = True
    article.save()
    return HttpResponseRedirect('/admin/article/published')


# 文章取消置顶
# @login_required(login_url='/admin/login')
def ArticleUnTopHandler(request, article_id):
    article = Article.objects.get(id=article_id)
    article.topped = False
    article.save()
    return HttpResponseRedirect('/admin/article/published')


'''
文章标签、分类管理
'''


# @login_required(login_url='/admin/login')
def CategoryList(request):
    template_name = 'control/attr/list.html'

    context = {'list': Category.objects.all(), 'page_type': 'category'}

    return render(request, template_name, context)


# @login_required(login_url='/admin/login')
def CategoryAddHandler(request):
    if request.method == 'POST':
        cate = Category()
        # cate.id = GetIDBasedOnTime()
        cate.name = request.POST.get('new_cate', ' ')
        cate.save()

    return HttpResponseRedirect('/admin/attr/category')


# @login_required(login_url='/admin/login')
def CategoryEditHandler(request):
    if request.method == 'POST':
        cate = Category.objects.get(id=request.POST.get('id'))
        cate.name = request.POST.get('name')
        cate.save()
    return HttpResponseRedirect('/admin/attr/category')


# @login_required(login_url='/admin/login')
def CategoryDelHandler(request):
    if request.method == 'POST':
        Category.objects.get(id=request.POST.get('id')).delete()
    return HttpResponseRedirect('/admin/attr/category')


# @login_required(login_url='/admin/login')
def TagList(request):
    template_name = 'control/attr/list.html'

    context = {'list': Tag.objects.all(), 'page_type': 'tag'}

    return render(request, template_name, context)


# @login_required(login_url='/admin/login')
def TagAddHandler(request):
    if request.method == 'POST':
        tag = Tag()
        # tag.id = GetIDBasedOnTime()
        tag.name = request.POST.get('new_tag', ' ')
        tag.save()

    return HttpResponseRedirect('/admin/attr/tag')


# @login_required(login_url='/admin/login')
def TagEditHandler(request):
    if request.method == 'POST':
        tag = Tag.objects.get(id=request.POST.get('id'))
        tag.name = request.POST.get('name')
        tag.save()
    return HttpResponseRedirect('/admin/attr/tag')


# @login_required(login_url='/admin/login')
def TagDelHandler(request, method='POST'):
    if request.method == 'POST':
        Tag.objects.get(id=request.POST.get('id')).delete()
    return HttpResponseRedirect('/admin/attr/Tag')
