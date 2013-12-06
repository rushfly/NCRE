#coding=utf8
from django.contrib import admin
from NCRE.models import NCRE, TestScore


class NCREAdmin(admin.ModelAdmin):
    list_display = ('id', 'testDate', 'place')
    ordering = ('id',)


class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('testId', 'stuName', 'certId')
    list_filter = ('ncre',)


admin.site.register(NCRE, NCREAdmin)
admin.site.register(TestScore,TestScoreAdmin)