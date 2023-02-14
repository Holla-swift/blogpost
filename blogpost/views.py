from django.shortcuts import render, redirect
from django.db.models import Q
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

def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render (request, 'post.html', context)

def about(request):
    return render (request, 'about_page.html')

def category_post_list(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories_in=[category])
    context = {
        'posts': posts,
    }
    return render (request, 'post_list.html', context)

def all_posts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render (request, 'all_posts.html', context)

#search
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title_icontains = query) |
            Q(overview_icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render (request, 'search_results.html', context)