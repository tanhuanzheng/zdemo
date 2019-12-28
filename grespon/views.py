from django.http import HttpResponse, JsonResponse


def index(request):

    return HttpResponse('hello', 202)


def hrespon(request):    # 使用属性赋值的方法返回HttpResponse对象
    response = HttpResponse()
    response['aa'] = 'bb'
    response['Host'] = request.get_host()
    response.content = 'hello'
    response.status_code = 403
    return response


def jrespon(request):   # 使用JsonResponse返回json对象

    return JsonResponse({'city': 'beijing', 'subject': 'python'})

