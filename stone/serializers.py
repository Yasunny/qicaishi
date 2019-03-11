# coding:utf-8
"""
@Author:LiuHuanan
@Date:2018/12/2
"""
from rest_framework import serializers

from stone.models import Book, UserInfo


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        # exclude = ('ug')
        # depth = 1

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ['id', 'name','price','publish_time']
