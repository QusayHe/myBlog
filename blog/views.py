from django.db.models import Count
from django.shortcuts import render
from .models import *
from django.core.signing import TimestampSigner


# Create your views here.


def index(request):
    # 分类
    categories = Category.objects.all()
    # 文章
    articles = Article.objects.all()
    # 标签
    tags = Tag.objects.all()
    # 最新文章
    new_articles = Article.objects.order_by('-created_time').all()[:5]
    # 归档
    archive_article = Article.objects.datetimes('published_time', 'month', order='DESC')

    """
    SELECT YEAR(articleTime) AS 'year',MONTH(articleTime) AS 'month',COUNT(*) AS 'count' FROM article 
    GROUP BY YEAR(articleTime) DESC,MONTH(articleTime);
    """
    return render(request, 'blog/index.html', context={
        'archive_article': archive_article,
        'new_articles': new_articles,
        'tags': tags,
        'articles': articles,
        'categories': categories})


def detail(request):

    signer=TimestampSigner()
    print(signer.sign('hello'))
    return render(request, 'blog/single.html');