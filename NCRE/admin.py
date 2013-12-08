#coding=utf8

from datetime import datetime
from django.contrib import admin
from NCRE.models import NCRE, TestScore, QueryCount



class NCREAdmin(admin.ModelAdmin):
    list_display = ('id', 'testDate', 'place')
    ordering = ('id',)

	
class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('testId', 'stuId', 'stuName', 'paper_score', 'score', 'certId')
    list_filter = ('ncre',)


admin.site.register(NCRE, NCREAdmin)
admin.site.register(TestScore,TestScoreAdmin)
admin.site.register(QueryCount)

