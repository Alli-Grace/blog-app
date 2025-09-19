from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>/', views.post, name='post'),
    path('create-post/', views.create_post, name='create_post'),
    path('edit/<str:pk>/', views.edit_post, name='edit_post'),
    path('delete/<str:pk>/', views.delete_post, name='delete_post')

]