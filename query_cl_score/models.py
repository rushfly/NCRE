#coding=utf-8
from django.db import models


# Create your models here.
class TestInfo(models.Model):
    testId = models.CharField(max_length=16, verbose_name=u'准考证号', unique=True)
    stuName = models.CharField(max_length=12, verbose_name=u'姓名')
    stuId = models.CharField(max_length=18, verbose_name=u'身份证')
    score = models.FloatField(verbose_name=u'成绩')
    level = models.IntegerField(verbose_name=u'成绩等第')
    certId = models.CharField(max_length=14, verbose_name=u'证书编号', null=True, blank=True)

    def __unicode__(self):
        return self.testId
