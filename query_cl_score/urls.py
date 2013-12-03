from django.conf.urls import patterns, url
from query_cl_score import views

urlpatterns = patterns(
    '',
    url(r'^check/$', views.check),
    url(r'^result/$',views.show_result),
    url(r'^import/$',views.import_dbf),
)