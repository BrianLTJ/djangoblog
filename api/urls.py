from django.conf.urls import url
from api import articles, categories, tags

urlpatterns = [
    url(r'manage/article', articles.api_article_entrance),
    url(r'manage/category', categories.api_category_entrance),
]
