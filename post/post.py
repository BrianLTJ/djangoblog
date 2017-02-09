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

    resdata['status']='ok'
    resdata['post_id']='test_post_id'

    return JsonResponse(resdata)


