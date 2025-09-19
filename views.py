# from .models import Post
# from main.models import CustomUser
# from django.contrib import messages
# from django.shortcuts import get_object_or_404, redirect, render
# from django.http import HttpResponseForbidden

# # Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', {'posts':posts})

# def post(request, pk):
#     posts = Post.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts':posts})

# def create_post(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         body = request.POST.get('body')
#         post = Post.objects.create(
#             title = title,
#             body = body
#         )
#         return redirect('index')
#     return render(request, 'create_post.html')

# def update_post(request, pk):
#     post = get_object_or_404(Post, pk)

#     if request.method == 'POST':
#         title = request.POST.get('title')
#         body = request.POST.get('body')

#         post.title = title
#         post.body = body

#         post.save()

#         return redirect('index')
#     return render(request, 'update_post.html', {'post':post})


# def delete_post(request, pk):
#     if request.method == 'POST':
#         post = get_object_or_404(Post, pk)
#         post.delete()
#         return redirect('index')
    
#     return HttpResponseForbidden

# def comment_on_post(request, pk):
#     post = get_object_or_404(Post, pk)

#     return render(request, 'comment.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .models import CustomUser
# from django.utils import timezone
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
# from django.utils.crypto import get_random_string


# # Create your views here.
# def signup_view(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = CustomUser.objects.create_user(
#             first_name = first_name,
#             email=email,
#             password=password
#         )
#         # is_member = True
#         user.save()
#         login(request, user)
#         messages.success('Signup successful')
#         return redirect('login')
    
#     return render(request, 'signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful')
#             return redirect('index')
#         else:
#             messages.error('Invalid Credentials')

#     return render(request, 'login.html')


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('post/<str:pk>/', views.post, name='post'),
#     path('post-create/', views.create_post, name='create_post'),

# ]






