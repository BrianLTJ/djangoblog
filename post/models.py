from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField('标题', null=True)
    article_id = models.IntegerField('文章id', null=False)
    content = models.TextField('内容', null=True)
    content_type = models.CharField('内容类型', default='h',max_length=2)
    update_time = models.DateTimeField('更新时间', null=False, auto_now=True)
    status = models.CharField('文章状态', null=False,default='d' , max_length=2)
    visibility = models.CharField('可见性', null=False, default='p', max_length=2)
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

