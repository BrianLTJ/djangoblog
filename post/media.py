from django.shortcuts import render
from django.http import HttpResponse
from post.models import Article, Tag, Category


def media_index(request):
    return render(request, 'post/media/index.html')