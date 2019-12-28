import json
from django.http import HttpResponse


def index(request):  # 非表单类型的请求体数据，Django无法自动解析，
                    # 可以通过request.body属性获取最原始的请求体数据，
                    # 自己按照请求体格式（JSON、XML等）进行解析。request.body返回bytes类型。
    str1 = request.body
    json_str = json.loads(str1.decode())
    print(json_str)  # bytes类型
    a = json_str['a']
    b = json_str['b']
    return HttpResponse('OK-----a=%s  b=%s' % (a, b))
