#coding=utf8
from datetime import datetime

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from NCRE.models import NCRE, TestScore, QueryCount


class TestDateListFilter(admin.SimpleListFilter):
    title = _(u'考试日期')
    parameter_name = 'test_date'

    def lookups(self, request, model_admin):
        ncres = NCRE.objects.all()
        dates = ((ncre, ncre.testDate) for ncre in ncres)
        return dates

    def queryset(self, request, queryset):
        return queryset.filter(ncre=self.value())


class NCREAdmin(admin.ModelAdmin):
    list_display = ('testDate', 'place')
    ordering = ('id',)


class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('testId', 'stuName', 'paper_score', 'score', 'certId', 'test_date')


admin.site.register(NCRE, NCREAdmin)
admin.site.register(TestScore, TestScoreAdmin)
admin.site.register(QueryCount)