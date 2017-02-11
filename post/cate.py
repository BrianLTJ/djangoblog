from django.shortcuts import render
from post.models import Category
from django.http import JsonResponse


def cate_index(request):
    return render(request, 'post/post_cate.html')


def cate_handler(request):
    defres = list()
    defres['result'] = 'error'
    res=defres
    reqdata=request.POST
    if reqdata.get('method')=='add':
        res=cate_new(request.POST)
    elif reqdata.get('method'=='list'):
        res=cate_list()
    return JsonResponse(res)

def cate_new(req_json):
    cate = Category
    cate.name=req_json.get('name')

    cate.save()
    res=list()
    res['result']='ok'
    return res


def cate_list():
    items = Category.objects.all()
    return items

