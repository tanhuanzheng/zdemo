from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect


def index(request):

    return HttpResponse('hello', 202)


def hrespon(request):    # 使用属性赋值的方法返回HttpResponse对象
    response = HttpResponse()
    response['aa'] = 'bb'
    response['Host'] = request.get_host()
    response.content = 'hello'
    response.status_code = 302
    return response


def jrespon(request):   # 使用JsonResponse返回json对象

    return JsonResponse({'city': 'beijing', 'subject': 'python'})


def rdirect(request):

    return redirect('http://www.baidu.com')


def cookie_index(request):
    rep = HttpResponse('OK')
    # rep.set_cookie(key='ck1', value='11111', max_age=1000)
    # rep.set_cookie(key='ck2', value='2222222', max_age=1000)
    # rep.set_cookie(key='ck3', value='333333', max_age=1000)
    ck = request.COOKIES
    print(ck)
    rep.content = ck
    return rep


