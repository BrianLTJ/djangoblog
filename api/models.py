from django.db import models


class Category(models.Model):
    name = models.TextField(null=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.TextField(null=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

# 专题
class Topic(models.Model):
    name = models.TextField(null=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    image = models.TextField('介绍图', null=True)
    body = models.TextField('正文-markdown', null=True)
    text = models.TextField('正文-纯文字', null=True)
    status = models.CharField('文章状态', max_length=10)
    visibility = models.CharField('文章可见性', max_length=10)
    topped = models.BooleanField('置顶', default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ForeignKey('Tag', verbose_name='标签', blank=True)
    topic = models.ForeignKey('Topic', verbose_name='专栏', blank=True)

