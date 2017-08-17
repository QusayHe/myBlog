from django.shortcuts import render
from .models import Category

# Create your views here.


def index(request):
    categories = Category.objects.get(id=1)
    return render(request, 'blog/index.html', context={'categories': categories})