#coding=utf8
from django.db import models


# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=10, verbose_name=u'姓名')
    test_id = models.CharField(max_length=12, verbose_name=u'考号', unique=True)

    def __unicode__(self):
        return self.stu_name

    class Meta:
        verbose_name = u'学生信息'
        verbose_name_plural = u'学生信息'


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=10, verbose_name=u'姓名')

    def __unicode__(self):
        return self.teacher_name

    class Meta:
        verbose_name_plural = u'教师信息'
        verbose_name = u'教师信息'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=20, verbose_name=u'课程名称')
    teacher = models.ForeignKey(Teacher, verbose_name=u'教师', null=True, blank=True)

    def __unicode__(self):
        return self.lesson_name

    class Meta:
        verbose_name_plural = '课程信息'
        verbose_name = u'课程信息'


class Score(models.Model):
    student = models.ForeignKey(Student)
    level_score = models.CharField(max_length=3, verbose_name=u'成绩', null=True, blank=True)
    score = models.FloatField(verbose_name=u'成绩', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name=u'课程')

    class Meta:
        verbose_name_plural = u'成绩'
        verbose_name = u'成绩'
        unique_together = ('student', 'lesson')

