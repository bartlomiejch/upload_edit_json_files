from django.conf.urls import patterns, url

urlpatterns = patterns('p2_homework.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^specific_document/(?P<document_id>\d+)/$', 'specific_document', name='specific_document'),
    url(r'^edit/(?P<document_id>\d+)/$', 'edit', name='edit'),
    
)
