from django.shortcuts import render
from django.http import HttpResponse
from post.models import Article, Tag, Category


# Create your views here.
def post_dashboard_index(request):
    return render(request, 'post/post_index.html')


def post_list_page(request):
    return render(request, 'post/post_list.html')


def post_detail_page(request, post_item_id):
    data = {'post_id': post_item_id}
    return render(request, 'post/post_detail.html', data)


def post_new_post(request):
    return render(request, 'post/post_detail.html')


def post_cate_page(request):
    return render(request, 'post/post_cate.html')


def post_tag_page(request):
    return render(request, 'post/post_tag.html')
