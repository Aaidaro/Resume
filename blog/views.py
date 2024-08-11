from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

def blog_main_view(request):
    published_posts = Post.objects.filter(status= 1, published_date__lte= datetime.now())
    draft_posts = Post.objects.filter(status= 0)
    context = {'published_posts':published_posts, "draft_posts":draft_posts}
    return render(request, 'blog/blog_main.html', context)

def single_blog_view(request, pid):
    published_posts = Post.objects.filter(status= 1, published_date__lte= datetime.now())
    post = get_object_or_404(published_posts, pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog_single.html', context)

# def test_view(request, pid):
#     post = Post.objects.get(id=pid)
#     context = {'post':post}
#     return render(request, 'blog/test.html', context)

