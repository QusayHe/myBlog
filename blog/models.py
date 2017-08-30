from django.db import models
from django.contrib.auth.models import *
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    title = models.CharField('标题', max_length=70)

    body = RichTextField(blank=True, null=True, verbose_name="正文")

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间')
    published_time = models.DateTimeField('发布时间')

    summary = models.CharField(verbose_name='摘要', max_length=200, blank=True)
    category = models.ForeignKey('Category', verbose_name='分类')
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者')
    isPublished = models.BooleanField(default=False, verbose_name='是否发布')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

