# coding:utf-8
"""
@Author:LiuHuanan
@Date:2018/11/18
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from stone import views

router = routers.DefaultRouter()

# router.register(r'^', views.UserInfoViewSet)
# router.register(r'^', views.BookListViewSet)
#
urlpatterns = [
    path('', views.hello, name='hello'),
    path('addbook/', views.addBook, name='addBook'),
    path('book_list/', views.book_list, name='book_list'),

]

# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
