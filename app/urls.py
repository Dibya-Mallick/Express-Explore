from django.urls import path
from . import views

urlpatterns=[
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('counter',views.counter, name='counter'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('back',views.back, name='back'),
    path('post/<str:pk>',views.post, name='post'), #dynamic url(like profile page for different users)
    path('read',views.read, name='read'),
    path('go_to_read',views.go_to_read, name='go_to_read'),
    path('go_to_home',views.go_to_home, name='go_to_home'),
    path('blog/<str:pk>',views.blog, name='blog'),
    path('go_to_explore',views.go_to_explore, name='go_to_explore'),
    path('explore',views.explore, name='explore'),
]   