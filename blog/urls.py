
from django.contrib import admin
from django.urls import path
from blogpost.views import (
    homepage, 
    post, 
    about, 
    #search, 
    category_post_list, 
    all_posts,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>', post, name = 'post'),
    path('about/', about, name = 'about'),
    path('postlist/<slug>', category_post_list, name = 'category_post_list'),
    path('post/', all_posts, name = 'all_posts'),
]
