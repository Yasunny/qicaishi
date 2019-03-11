import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from stone import models, serializers
# from  .models  import  book
from stone.models import Book
from stone.serializers import BookSerializer


def hello(request):
    return HttpResponse("hello world ,this is my first project")


def addBook(request):
    book_data = json.loads(request.body)

    try:
        # book.create(name = book_data['name'], price = book_data['price'], publishe_time=book_data['publish_time'])
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse("fail")

# def book_post(request):
#     if request.method == "post":
#         form = book_post(request.POST)
#
#         if form.is_vilid():
#             sbuject = form.cleaned_data.get("sbuject")
#             if sbuject =="数学":
#                 return HttpResponse("yes it is")
#             else:
#                 return HttpResponse("no it is not")
#             # return HttpResponse("成功")
#         else:
#             return HttpResponse("失败")

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = models.UserInfo.objects.all().order_by('-id')
    serializer_class = serializers.UserInfoSerializer


@csrf_exempt
@api_view(['GET','POST'])
def book_list(request):
    """
    List all book list, or create a new book list.
    """
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
