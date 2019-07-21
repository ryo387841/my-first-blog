from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),#一覧
    path('user/', views.user_index,name='user_index'),#一覧
    path('user/create/', views.user_create,name='user_create'),#一覧
    path('division/', views.division_index,name='division_index'),#一覧
    path('division/create/', views.division_create,name='division_create'),#一覧
    path('content/', views.content_index,name='content_index'),#一覧
    path('content/create/', views.content_create,name='content_create'),#一覧



    #path('read/', views.read,name='read'),#一覧
    #path('update/', views.update,name='update'),#一覧
    #path('delete/', views.delete,name='delete'),#一覧

    #path('users/add/', views.users,name='users')

]
