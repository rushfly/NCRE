#coding=utf8
# Create your views here.
import random
import uuid
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import xlrd
from NCRE import task

from NCRE.func import media_exist, handle_uploaded_file
from cntest.settings import MEDIA_ROOT
from NCRE.forms import CheckForm, UploadDbfForm
from NCRE.models import TestScore, NCRE, QueryCount


def check(request):
    opr1 = random.randint(1, 10)
    opr2 = random.randint(1, 10)
    error = ''
    if not cache.get('query_count'):
        count = QueryCount.objects.all()
        if not count:
            count = QueryCount.objects.create(q_count=0)
        cache.set('query_count', count.q_count, 3600 * 24)

    if request.GET:
        form = CheckForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            testid = cd['testId']
            captcha = cd['captcha']
            stu_id_four = cd['stuId']
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
                    if stu_id_four != info[0].stuId[-4:]:
                        error = 'id_error'
                    else:
                        cache.incr('query_count')
                        return render_to_response('NCRE/result.html', {'info': info[0]})
                else:
                    error = 'notfound'
            else:
                error = 'captcha_error'
    else:
        form = CheckForm()
    request.session['captcha'] = opr1 + opr2
    return render_to_response('NCRE/check.html', {'opr1': opr1, 'opr2': opr2, 'error': error, 'form': form,
                                                  'query_count': cache.get('query_count')})


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
    form = UploadDbfForm()
    if request.method == 'POST':
        form = UploadDbfForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['dbf_file']
            file_name = str(uuid.uuid1())
            file_name = 'cntest/dbf/%s.dbf' % file_name[:8]
            if not media_exist(file_name):
                handle_uploaded_file(request.FILES['dbf_file'], file_name)
            cd = form.cleaned_data
            ncre_id = cd['ncre']
            ncre = NCRE.objects.get(id=ncre_id)
            if media_exist(file_name):
                task.import_score(file_name, ncre)  # 异步执行导入过程
            return HttpResponse(u'导入成功')
    return render_to_response('NCRE/import_ncre_score.html', locals(),
                              context_instance=RequestContext(request))


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(manage_view))
            else:
                # Return a 'disabled account' error message
                errorMsg = "该用户已被禁用"
        else:
            # Return an 'invalid login' error message.
            errorMsg = "用户名或密码不正确"
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponse("Log out!")


def manage_view(request):
    return render_to_response('manage.html', locals(), context_instance=RequestContext(request))
