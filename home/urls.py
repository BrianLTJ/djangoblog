from django.conf.urls import url
from home import views


urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^', views.view_post, name='blog_view_post'),
]
