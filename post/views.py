from .models import Post, Comment
from account.models import CustomUser
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .forms import CommentForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.

def index(request):
    user = request.user
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        posts = Post.objects.all()
    context = {
        'posts':posts,
        'user': user
    }
    return render(request, 'index.html', context=context)

def post(request, pk):
    post = Post.objects.get(id=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name = form.cleaned_data['name'],
                body = form.cleaned_data['body'],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)

    context = {
        'post':post,
        'comments':comments,
        'form': CommentForm(),
     }
    return render(request, 'post.html', context=context)

def create_post(request):
    if request.method == 'POST':
        # user = CustomUser.objects.get(id=pk)
        user = request.user
        title = request.POST.get('title')
        body = request.POST.get('body')
        post = Post.objects.create(
            title = title,
            body = body,
            author = user
        )
        return redirect('index')
    return render(request, 'create_post.html')

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if request.method == 'POST':
        if not user:
            return messages.error(request, 'You do not have the permission to edit this post')
        else:
            title = request.POST.get('title')
            body = request.POST.get('body')

            post.title = title
            post.body = body

            post.save()
        return redirect('index')
        
    return render(request, 'edit_post.html', {'post':post})


def delete_post(request, pk):
    user = request.user
    if request.method == 'POST':
        if not user:
            return messages.error(request, 'You do not have the permission to delete this post')
        else:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
        return redirect('index')
    
    return HttpResponseForbidden


