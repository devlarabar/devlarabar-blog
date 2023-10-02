from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post
from django.contrib.auth.decorators import login_required
import core.helpers.request_helpers as helpers
from blog.forms.blog_forms import CreatePost


def index(request):
    context = helpers.prepare_context(request)
    context['title'] = 'Blog'
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'blog/index.html', context=context)


@login_required(login_url="/login/")
def create_post(request):
    context = helpers.prepare_context(request)
    if not context['admin']:
        return render(request, 'core/accessdenied.html', context=context)

    context['form'] = CreatePost(None)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags').split(', ')
        author_id = helpers.get_user_id(request)

        new_post = Post(
            title=title,
            content=content,
            tags=tags,
            date_posted=timezone.now(),
            author_id=author_id
        )
        new_post.save()

        print(f"Blog post created: {title}")

    return render(request, 'blog/createpost.html', context=context)


def view_post(request, post_id):
    context = helpers.prepare_context(request)

    post = Post.objects.get(id=post_id)
    context['post'] = post

    return render(request, 'blog/viewpost.html', context=context)


@login_required(login_url="/login/")
def edit_post(request, post_id):
    context = helpers.prepare_context(request)
    if not context['admin']:
        return render(request, 'core/accessdenied.html', context=context)

    post = Post.objects.get(id=post_id)
    context['post'] = post

    initial_form_data = {
        'title': post.title,
        'content': post.content,
        'tags': ", ".join(post.tags)
    }

    context['form'] = CreatePost(initial=initial_form_data)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags').split(', ')

        post.title = title
        post.content = content
        post.tags = tags
        post.save()

        print(f"Blog post updated: {title}")

        return redirect(view_post, post_id=post_id)

    return render(request, 'blog/editpost.html', context=context)
