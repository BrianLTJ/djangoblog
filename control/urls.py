from django.conf.urls import url
from control import views

urlpatterns = [
    url(r'^/article/all$', views.ArticleAll.as_view(), name='article_all'),
    url(r'^/article/published$', views.ArticlePublished.as_view(), name='article_published'),
    url(r'^/article/draft$', views.ArticleDraft.as_view(), name='article_draft'),
    url(r'^/article/recycle$', views.ArticleRecycle.as_view(), name='article_recycle'),
    url(r'^/article/edit/(?P<article_id>\d+)$', views.ArticleEdit.as_view(), name='article_edit'),
]