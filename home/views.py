from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index/index.html')


def view_post(request):
    return render(request, 'home/post/detail.html')
