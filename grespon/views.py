from django.http import HttpResponse


def index(request):

    return HttpResponse('hello', 202)


def index2(request):    # 使用属性赋值的方法返回HttpResponse对象
    response = HttpResponse()
    response['aa'] = 'bb'
    response['Host'] = request.get_host()
    response.content = 'hello'
    response.status_code = 403
    return response
