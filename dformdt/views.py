from django.http import HttpResponse


def index(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    return HttpResponse('it\'s ok  a=%s  b=%s  alist=%s' % (a, b, alist))
