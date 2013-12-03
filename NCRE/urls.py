from django.conf.urls import patterns, url
from NCRE import views

urlpatterns = patterns(
    '',
    url(r'^check/$', views.check),
    url(r'^import/xls/$',views.import_xls),
    url(r'^import/dbf/$',views.import_dbf),
)
