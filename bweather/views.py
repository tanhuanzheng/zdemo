from django.http import HttpResponse


def index(request):    # 访问首页

    return HttpResponse('hello world')


def index2(request, year, city):  # 获取路径参数
    print(city+year)
    return HttpResponse('it\'s ok, city=%s, year=%s' % (city, year))
