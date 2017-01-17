"""
文章相关操作
Create
Read
Update
Delete

Required field: method

"""
from api import models
from django.http import JsonResponse
import json

# 文章API入口
def api_article_entrance(request):
    data = list()
    item = dict()
    item['title'] = '测试标题'
    item['body'] = 'test文章主体'
    # item_str = json.dumps(item)
    # data.append(item_str)
    data.append(item)
    item['title'] = '测试标题2'
    item['body'] = 'test文章2主体'
    # item_str = json.dumps(item)
    # data.append(item_str)
    data.append(item)
    item['title'] = '测试标题3'
    item['body'] = 'test3文章主体'
    # item_str = json.dumps(item)
    # data.append(item_str)
    data.append(item)

    return JsonResponse(data, safe=False)
