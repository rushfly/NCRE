# Create your views here.
import random
from django.http import HttpResponse
from django.shortcuts import render_to_response
import xlrd
from cntest.settings import MEDIA_ROOT
from query_cl_score.forms import CheckForm
from query_cl_score.models import TestInfo


def check(request):
    opr1 = random.randint(1, 10)
    opr2 = random.randint(1, 10)
    error = ''
    if request.GET:
        form = CheckForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            testid = cd['testId']
            captcha = cd['captcha']
            try:
                captcha = int(captcha)
            except ValueError:
                captcha = -1
            if request.session['captcha'] == captcha:
                info = TestInfo.objects.filter(testId=testid)
                if info:
                    request.session['captcha'] = opr1 + opr2
                    return render_to_response('cntest/result.html', {'info': info[0]})
                else:
                    error = 'notfound'
            else:
                error = 'captcha_error'
    else:
        form = CheckForm()
    request.session['captcha'] = opr1 + opr2
    return render_to_response('cntest/check.html', {'opr1': opr1, 'opr2': opr2, 'error': error, 'form': form})


def show_result(request):
    return None


def import_dbf(request):
    book = xlrd.open_workbook(MEDIA_ROOT + 'cntest/score.xls')
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        testid = sheet.cell(row, 1).value
        stuname = sheet.cell(row, 3).value
        stuid = sheet.cell(row, 5).value
        score = sheet.cell(row, 10).value
        level = sheet.cell(row, 11).value
        certid = sheet.cell(row, 14).value
        TestInfo.objects.create(testId=testid, stuName=stuname, stuId=stuid, score=score, level=level,
                                certId=certid)
    return HttpResponse('Import sucess!')