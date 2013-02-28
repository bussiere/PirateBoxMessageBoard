from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^Jackpoint/', include('foo.urls')),
    url(r'^$', 'message.views.index',name='message-index'),
    url(r'message/(\d+)$', 'message.views.message',name='message-message'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
handler404 = 'message.views.my_404'
