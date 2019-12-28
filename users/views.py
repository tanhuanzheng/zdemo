from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):

    return HttpResponse('hello hello world')


def index_one(request):

    return HttpResponse('i am index_one')


def index_two(request):
    url = reverse("two")
    print('path=', url)

    return HttpResponse('i am index_two')
