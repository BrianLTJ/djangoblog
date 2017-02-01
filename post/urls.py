from django.conf.urls import url
from post import post as post_views


urlpatterns =[
    url(r'post/list', post_views.post_list_page, name='dashboard_post_list'),
    url(r'post/detail/(?P<post_item_id>[0-9]+)', post_views.post_detail_page, name='dashboard_post_detail'),
    url(r'post/category', post_views.post_cate_page, name='dashboard_cate'),
    url(r'post/tag', post_views.post_tag_page, name='dashboard_tag'),
    url(r'', post_views.post_dashboard_index, name='dashboard_index'),
]