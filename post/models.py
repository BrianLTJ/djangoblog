from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.TextField('标题', null=True)
    article_id = models.IntegerField('文章id', null=False)
    content = models.TextField('内容', null=True)
    content_type = models.CharField('内容类型', default='h',max_length=2)
    update_time = models.DateTimeField('更新时间', null=False, auto_now=True)
    '''
    文章状态:
    p 已发布
    d 草稿
    r 回收站
    (Future)h 历史版本
    '''
    status = models.CharField('文章状态', null=False,default='d', max_length=2)
    '''
    可见性
    p 公开
    (Future)s 仅本人可见
    '''
    visibility = models.CharField('可见性', null=False, default='p', max_length=2)
    '''
    根据文字内容等生产的hash
    未来与历史版本功能一起
    '''
    hash = models.CharField('文章hash code', max_length=10, null=True)
    top = models.BooleanField('是否置顶', default=False)

    category = models.ForeignKey('Category', null=True)
    tag = models.ForeignKey('Tag', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['article_id', '-update_time']


class Category(models.Model):
    name = models.CharField('名称', null=True, max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', null=True, max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

