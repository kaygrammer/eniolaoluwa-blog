from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Post, Comment, Aboutme
from .forms import CommentForm, EmailPostForm, SearchForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector


def post_list(request):
    posts = Post.published.all()[:3]
    blogger = User.objects.get()
    context = {'posts': posts,
               'blogger':blogger,}
    return render(request, 'blog/post/index.html', context)


def all_post(request, tag_slug=None):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator,page(paginator.num_pages)

    #tag = None
    #if tag_slug:
        #tag = get_object_or_404(Tag, slug=tag_slug)
        #posts = posts.filter(tags__in=[tag])
    context = {'posts': posts,
               'page':page,
               #'tag':tag,
               }
    return render(request, 'blog/post/allpost.html', context)


def post_detail(request,id, tag_slug=None):
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

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        first_post = first_post.filter(tags__in=[tag])

    context = {
        'first_post':first_post,
        'post':post,
        'next':next,
        'prev':prev,
        'comments':comments,
        'comment_form':comment_form,
        'new_comment':new_comment,
        'tag':tag,

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


def share_post(request,  post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def AboutMePage(request):
    about = get_object_or_404(Aboutme, status='published')
    return render(request, 'blog/post/about.html', {'about': about})


def ContactPage(request):
    return render(request, 'blog/post/contact.html')


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,'blog/post/detail.html', {'form': form,'query': query,'results': results})






