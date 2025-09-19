from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('members/', views.get_members, name='members'),

    # path('post-create/', views.create_post, name='create_post'),

]