from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'cntest.views.home', name='home'),
    # url(r'^cntest/', include('cntest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
    url(r'^pclevel/', include('NCRE.urls')),
    url(r'^$', 'NCRE.views.check'),
    url(r'^test/$','celerytest.views.test'),
    url(r'^login/$', 'NCRE.views.login_view'),
    url(r'^logou/$', 'NCRE.views.logout_view'),
    url(r'^manage/$', 'NCRE.views.manage_view'),
    url(r'^qrcode/$','qr_code.views.my_qr'),
    url(r'^mycode/$',TemplateView.as_view(template_name='qrcode/qrcode.html')),
)
