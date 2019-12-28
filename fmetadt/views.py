from django.http import HttpResponse
# 可以通过request.META属性获取请求头headers中的数据，request.META为字典类型


def index(request):
    metadt = request.META['REMOTE_ADDR']
    print(metadt)
    return HttpResponse('OK------META=%s' % metadt)
