from django.conf.urls import url
from control import views

urlpatterns = [
    url(r'^$', views.Index, name='control_index'),

    url(r'^/login$', views.login_index, name='control_login_index'),
    url(r'^/login/handler/login$', views.login_handler, name='control_login_handler'),
    url(r'^/login/handler/logout$', views.logout_handler, name='control_logout_handler'),

    url(r'^/article$', views.ArticleList, {'page_type': 'all'}, name='article_index'),
    url(r'^/article/handler/add$', views.ArticleAddHandler, name='article_add_handler'),
    url(r'^/article/add$', views.ArticleAdd, name='article_add'),

    url(r'^/article/all$', views.ArticleList, {'page_type': 'all'}, name='article_all'),
    url(r'^/article/published$', views.ArticleList, {'page_type': 'published'}, name='article_published'),
    url(r'^/article/draft$', views.ArticleList, {'page_type': 'draft'}, name='article_draft'),
    url(r'^/article/recycle$', views.ArticleList, {'page_type': 'recycle'}, name='article_recycle'),

    url(r'^/article/handler/edit$', views.ArticleEditHandler, name='article_edit_handler'),
    url(r'^/article/edit/(?P<article_id>\d+)$', views.ArticleEdit.as_view(), name='article_edit'),

    url(r'^/article/handle/del/(?P<article_id>\d+)', views.ArticleDelHandler, name='article_del_handler'),
    url(r'^/article/handle/recycle/(?P<article_id>\d+)', views.ArticleRecycleHandler, name='article_recycle_handler'),
    url(r'^/article/handle/publish/(?P<article_id>\d+)', views.ArticlePublishHandler, name='article_publish_handler'),
    url(r'^/article/handle/restore/(?P<article_id>\d+)', views.ArticleRestoreToDraftHandler, name='article_restore_handler'),

    url(r'^/article/handler/top/(?P<article_id>\d+)', views.ArticleTopHandler, name='article_top_handler'),
    url(r'^/article/handler/untop/(?P<article_id>\d+)', views.ArticleUnTopHandler, name='article_untop_handler'),

    url(r'^/attr$', views.CategoryList, name='attr_index'),
    url(r'^/attr/category$', views.CategoryList, name='attr_category'),
    url(r'^/attr/category/handler/add$', views.CategoryAddHandler, name='attr_category_add_handler'),
    url(r'^/attr/category/handler/edit$', views.CategoryEditHandler, name='attr_category_edit_handler'),
    url(r'^/attr/category/handler/del$', views.CategoryDelHandler, name='attr_category_del_handler'),

    url(r'^/attr/tag$', views.TagList, name='attr_tag'),
    url(r'^/attr/tag/handler/add$', views.TagAddHandler, name='attr_tag_add_handler'),
    url(r'^/attr/tag/handler/edit$', views.TagEditHandler, name='attr_tag_edit_handler'),
    url(r'^/attr/tag/handler/del$', views.TagDelHandler, name='attr_tag_del_handler'),
]