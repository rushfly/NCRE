#coding=utf8
from django import forms
from NCRE.models import NCRE


class CheckForm(forms.Form):
    testId = forms.CharField(max_length=18, label=u'准考证号', required=True,
                             widget=forms.TextInput(attrs={'class': 'input-medium', 'required': 'required'}))
    captcha = forms.IntegerField(label=u'验证码', required=True,
                                 widget=forms.TextInput(attrs={'class': 'input-mini', 'required': 'required'}))


class UploadDbfForm(forms.Form):
    tests = NCRE.objects.all()
    test_list = [(t.pk, t.testDate) for t in tests]
    import_to = forms.CharField(label=u'导入位置', widget=forms.Select(choices=test_list, attrs={'required': 'required'}))
    dbf_file = forms.FileField(label=u'DBF文件', widget=forms.FileInput(attrs={'required': 'required'}))