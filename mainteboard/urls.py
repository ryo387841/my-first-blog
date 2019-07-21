from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),#一覧
    path('create/', views.create,name='create'),#一覧
    path('read/<int:id>/', views.read,name='read'),#一覧
    path('update/<int:id>/', views.update,name='update'),#一覧
    path('delete/', views.delete,name='delete'),#一覧

    #path('users/add/', views.users,name='users')

]
