from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url('^score/query/$', 'article.views.query_score')
)
