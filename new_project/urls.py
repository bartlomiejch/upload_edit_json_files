from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^', include('p2_homework.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'new_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)
