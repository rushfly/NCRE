#coding=utf8
from django.contrib import admin
from NCRE.models import NCRE


class NCREAdmin(admin.ModelAdmin):
    list_display = ('id',  'testDate', 'place')
    ordering = ('id',)


admin.site.register(NCRE, NCREAdmin)
