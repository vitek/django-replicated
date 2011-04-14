from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'test_request', 'testapp.views.test_request'),
    (r'test_use_slave', 'testapp.views.test_use_slave'),
    (r'test_use_master', 'testapp.views.test_use_master'),

    # Example:
    # (r'^test_replicated/', include('test_replicated.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
