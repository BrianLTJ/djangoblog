from django.conf.urls import url
from post import post as post_views
from post import media as media_views


urlpatterns =[
    url(r'/post/list', post_views.post_list_page, name='dashboard_post_list'),
    url(r'/post/detail/(?P<post_item_id>[0-9]+)', post_views.post_detail_page, name='dashboard_post_detail'),
    url(r'/post/new', post_views.post_new_post, name='dashboard_new_post'),
    url(r'/post/category', post_views.post_cate_page, name='dashboard_cate'),
    url(r'/post/tag', post_views.post_tag_page, name='dashboard_tag'),

    url(r'/post/handler/add', post_views.post_add_handler, name='dashboard_new_post_handler'),

    url(r'/media$', media_views.media_index, name='dashboard_media_index'),

    url(r'', post_views.post_dashboard_index, name='dashboard_index'),
]
