from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


def post_list(request):
    posts = Post.published.all()[:3]
    blogger = User.objects.get()
    return render(request, 'blog/post/index.html', {'posts': posts,
                                                    'blogger': blogger})

def all_post(request):
    posts = Post.published.all()
    context = {'posts':posts}
    return render(request, 'blog/post/allpost.html', context)


def post_detail(request,id):
    first_post = Post.objects.all()[:3]
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        post = None
    try:
        next = Post.objects.get(id=id + 1)
    except Post.DoesNotExist:
        next = None
    try:
        prev = Post.objects.get(id=id - 1)
    except Post.DoesNotExist:
        prev = None

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'first_post':first_post,
        'post':post,
        'next':next,
        'prev':prev,
        'comments':comments,
        'comment_form':comment_form,
        'new_comment':new_comment

    }
    return render(request, 'blog/post/detail.html', context)

def update(request,post_id,id):
    comment = Comment.objects.get(id=id)
    if request.method =='POST':
        edit_form = CommentForm(instance=comment, data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "Comment edited successfully")
            return redirect("post_detail", id=post_id)
    else:
        edit_form = CommentForm(instance=comment)
    context = {'edit_form':edit_form}
    return render(request, 'blog/post/formedit.html', context)






