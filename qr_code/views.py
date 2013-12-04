#coding=utf8
from cStringIO import StringIO
from django.http import HttpResponse
import qrcode

# Create your views here.


def my_qr(request):
    response = HttpResponse()
    if request.method == 'GET':
        content = request.GET.get('content', '')
        if content:
            img = qrcode.make(content)
            temp = StringIO()
            img.save(temp)
            response = HttpResponse(temp.getvalue(), mimetype='image/png')
    return response

