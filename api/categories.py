"""
文章相关操作
Create
Read
Update
Delete

Required field: method

"""
from api import models
from api.models import Category
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_category_entrance(request):

    if 1:
        data = json.loads(request.body.decode("utf-8"))
        print(data['method'])
        try:
            if data['method'] == 'put':
                return category_create(data)
        except:
            error_response = dict()
            error_response['result'] = 'error'
            error_response['msg'] = 'Json data malformed'
            response = JsonResponse(error_response)
            response.status_code = 400
            return response
            pass
    else:
        error_response = dict()
        error_response['result'] = 'error'
        error_response['msg'] = 'Malformed request'
        response = JsonResponse(error_response)
        response.status_code=400
        return response

'''
# Create Category

POST:
{
    cate_name："CATE_NAME"
}

RESPONSE:
SUCCESS
{
    result: "success",
    cate_name："CATE_NAME",
    cate_id："CATE_ID"
}
FAIL
{
    result: "error",
}
'''
def category_create(data):
    cate_item = Category()
    cate_item.name = data['cate_name']
    resp = dict()
    status_code = 200
    if cate_item.save():
        resp['result'] = 'success'
        resp['cate_name'] = cate_item.name
        resp['cate_id'] = cate_item.id
        status_code = 200
    else:
        resp['result'] = 'error'
        status_code = 500

    response = JsonResponse(resp)
    response.status_code = status_code
    return response


# Read Category name and id
def category_get_name(request):
    return ""


def category_get_id(request):
    return ""


# Update category text
def category_update(request):
    return ""


'''
# Delete category

POST:
{
    cate_id: "CATE_ID"
}

RESPONSE:
SUCCESS
{
    result: "success"
}
FAIL
{
    result: "error",
    msg: "Category id CATE_ID not exists"
}
'''
def category_delete(request):
    return ""
