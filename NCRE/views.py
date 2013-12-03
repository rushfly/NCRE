#coding=utf8
# Create your views here.
import random
import uuid

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render_to_response
import xlrd
from dbfpy import dbf

from NCRE.func import media_exist, handle_uploaded_file
from cntest.settings import MEDIA_ROOT
from NCRE.forms import CheckForm, UploadDbfForm
from NCRE.models import TestScore


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
                if len(testid) == 16:
                    info = TestScore.objects.filter(testId=testid)
                else:
                    info = TestScore.objects.filter(stuId=testid)
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


def import_xls(request):
    book = xlrd.open_workbook(MEDIA_ROOT + 'cntest/score.xls')
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        testid = sheet.cell(row, 1).value
        stuname = sheet.cell(row, 3).value
        stuid = sheet.cell(row, 5).value
        score = sheet.cell(row, 10).value
        level = sheet.cell(row, 11).value
        certid = sheet.cell(row, 14).value
        TestScore.objects.create(testId=testid, stuName=stuname, stuId=stuid, score=score, level=level,
                                 certId=certid)
    return HttpResponse('Import sucess!')


def import_dbf(request):
    if request.Method == 'POST':
        form = UploadDbfForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['dbf_file']
            #5分钟内不能重复上传相同文件
            if not cache.get('time_stamp'):
                cache.set('time_stamp', uuid.uuid1(), 60 * 5)
            file_name = uuid.uuid3(cache.get('time_stamp'), file_obj.name)
            file_name = 'cntest/dbf/%s' % file_name
            if not media_exist(file_name):
                handle_uploaded_file(request.FILES, file_name)
            if media_exist(file_name):
                try:
                    db = dbf.Dbf(MEDIA_ROOT + file_name)
                    for rec in db:
                        stu_name = rec['XM']
                except:
                    return HttpResponse('无法导入')
            cd = form.cleaned_data

        return None