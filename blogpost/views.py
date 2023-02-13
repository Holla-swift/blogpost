from django.shortcuts import render, redirect
from .models import (
    Author,
    Category,
    Post
)

# Create your views here.
def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
        
    context = {
            'object_list': featured,
            'latest': latest,
            'categories': categories
    }
    return render (request, 'homepage.html', context)

def post(request):
    context = {
        
    }
    return render (request, 'homepage.html', context)

def about(request):
    context = {
        
    }
    return render (request, 'homepage.html', context)

def category_post_list(request):
    context = {
        
    }
    return render (request, 'homepage.html', context)

def all_posts(request):
    context = {
        
    }
    return render (request, 'homepage.html', context)