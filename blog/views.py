from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    tags = Tag.objects.all()
    new_articles = Article.objects.order_by('-created_time').all()[:5]

    return render(request, 'blog/index.html', context={
                                                        'newArticles': new_articles,
                                                        'tags': tags,
                                                        'articles': articles,
                                                        'categories': categories})