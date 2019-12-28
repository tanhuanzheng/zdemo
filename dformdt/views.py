from django.http import HttpResponse


def index(request):  # 前端发送的表单类型的请求体数据，可以通过request.POST属性获取，返回QueryDict对象
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    return HttpResponse('it\'s ok  a=%s  b=%s  alist=%s' % (a, b, alist))
