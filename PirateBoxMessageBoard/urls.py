from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^Jackpoint/', include('foo.urls')),
    url(r'^$', 'message.views.index',name='message-index'),  
    url(r'^404/$','message.views.my_404',name='message-404'),
    url(r'^message/(\d+)$', 'message.views.message',name='message-message'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^s/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/path/to/media'}),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
handler404 = 'message.views.my_404'
#handler500 = 'message.views.my_404'
