#coding=utf-8
from django.db import models


# Create your models here.
class NCRE(models.Model):
    testDate = models.DateField(verbose_name=u'考试时间')
    place = models.CharField(verbose_name=u'考试地点', max_length=20)
    stu_number = models.IntegerField(verbose_name=u'考试人数', null=True, blank=True)

    def __unicode__(self):
        return self.testName

    class Meta:
        verbose_name = u'计算机等级考试设置'
        verbose_name_plural = u'计算机等级考试设置'


class TestScore(models.Model):
    ncre = models.ForeignKey(NCRE)
    testId = models.CharField(max_length=16, verbose_name=u'准考证号', unique=True)
    stuName = models.CharField(max_length=12, verbose_name=u'姓名')
    stuId = models.CharField(max_length=18, verbose_name=u'身份证')
    score = models.FloatField(verbose_name=u'成绩')
    level = models.IntegerField(verbose_name=u'成绩等第')
    certId = models.CharField(max_length=14, verbose_name=u'证书编号', null=True, blank=True)

    def __unicode__(self):
        return self.testId
    class Meta:
        verbose_name_plural=u'考试成绩'
        verbose_name=u'考试成绩'