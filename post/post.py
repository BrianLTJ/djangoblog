from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from post.models import Article, Tag, Category


# Create your views here.
def post_dashboard_index(request):
    return render(request, 'post/post_index.html')


def post_list_page(request):
    return render(request, 'post/post_list.html')

@ensure_csrf_cookie
def post_detail_page(request, post_item_id):
    data = {'post_id': post_item_id}
    return render(request, 'post/post_detail.html', data)

@ensure_csrf_cookie
def post_new_post(request):
    return render(request, 'post/post_detail.html')


def post_cate_page(request):
    return render(request, 'post/post_cate.html')


def post_tag_page(request):
    return render(request, 'post/post_tag.html')


def post_add_handler(request):
    resdata = dict()
    if request.method=='POST':
        new_article=Article()
        reqdata=request.POST
        new_article.title=reqdata.get('title')
        new_article.beautified_url=reqdata.get('burl')
        new_article.content=reqdata.get('content')
        new_article.state=reqdata.get('post_state')
        new_article.visibility=reqdata.get('visibility')

        if reqdata.get('article_id') != None and reqdata.get('article_id') != '':
            # Have article_id
            new_article.article_id=reqdata.get('article_id')

            '''change this article_id posts into history'''
            old_posts=Article.objects.filter(article_id=new_article.article_id)
            for i in old_posts:
                i.state='h'
                i.save()

        else:
            '''
            Fetch a article id
            '''
            articlelist = Article.objects.all()
            articleidlist=list()
            for i in articlelist:
                if i.article_id not in articleidlist:
                    articleidlist.append(i.article_id)

            articleidlist=sorted(articleidlist)
            article_id=1
            if len(articleidlist)>0:
                article_id=articleidlist[len(articleidlist)-1]+1
            else:
                article_id=1

            new_article.article_id=article_id

        '''
        new_article.category = Category.objects.get(id=int(request.POST.get('category')))
        tags = request.POST.getlist('tags[]')
        new_article.tags.clear()
        for tag in tags:
            new_article.tags.add(Tag.objects.get(id=tag))

        '''

        new_article.save()

        resdata['result'] = 'ok'
        resdata['post_id'] = int(new_article.article_id)

        print('123')

        return JsonResponse(resdata)
    else:
        resdata['result'] = 'error000'
        return JsonResponse(resdata)





