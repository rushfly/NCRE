#coding=utf8
from django import forms


class CheckForm(forms.Form):
    testId = forms.CharField(max_length=16, label=u'准考证号', required=True,
                             widget=forms.TextInput(attrs={'class': 'input-medium', 'required': 'required'}))
    captcha = forms.IntegerField(label=u'验证码', required=True,
                                 widget=forms.TextInput(attrs={'class': 'input-mini', 'required': 'required'}))
