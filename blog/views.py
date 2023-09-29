from django.shortcuts import render
from blog.models import Post


def index(request):
    context = {
        'title': 'Blog'
    }
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'blog/index.html', context=context)
