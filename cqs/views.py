from django.http import HttpResponse


def index(request):  # 获取请求路径中的查询字符串参数（形如?k1=v1&k2=v2）
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    return HttpResponse('it\'s ok  a=%s,  b=%s,  alist=%s' % (a, b, alist))

