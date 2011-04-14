from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'test_request', 'testapp.views.test_request'),
    (r'test_use_slave', 'testapp.views.test_use_slave'),
    (r'test_use_master', 'testapp.views.test_use_master'),
)
