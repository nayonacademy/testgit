from django.urls import path
from . import views
urlpatterns = [
    path('login', views.bloglogin, name="login"),
    path('logout', views.bloglogout, name="logout"),
    path('', views.dashboard, name="dashboard"),
    path('posts', views.showAllpost, name='showallpost'),
    path('category', views.category, name='category'),
    path('posts/<int:pk>', views.updatePost, name='updatePost'),
    path('posts/delete/<int:pk>', views.postdelete, name='postdelete'),
    path('posts/add', views.newPost, name='newpost'),
    path('posts/update/<int:pk>', views.postupdate, name='postupdate'),
    path('settings', views.settings, name='settings')
]