from django.conf.urls import patterns, include, url
from django.conf import settings
# from moxisite.views import hello, current_datetime, hours_ahead
# from moxisite import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.LatestEntriesFeed import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moxisite.views.home', name='home'),
    # url(r'^moxisite/', include('moxisite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'moxisite.views.hello'),
    # url(r'^time/$', 'moxisite.views.current_datetime'),
    # url(r'^time/plus/(\d{1,2})/$', 'moxisite.views.hours_ahead'),
    # url(r'^search-form/$', views.search_form),
    # url(r'^search/$', views.search),
    # url(r'^contact/$', views.contact),
    url(r'^add_entry/$', 'blog.views.add_entry'),
    url(r'^entry/(?P<entry_id>\d+)/edit/$', 'blog.views.edit_entry', name='edit-entry'),
    url(r'^entry/(?P<entry_id>\d+)/delete/$', 'blog.views.delete_entry'),
    url(r'^$', 'blog.views.show_entries', name='home'),
    url(r'^thank/$', 'blog.views.thank'),
    url(r'^logout/$', 'blog.views.logout'),
    url(r'^entry/(?P<entry_id>\d+)/$', 'blog.views.entry'),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^accounts/login/$', 'blog.views.login'),
    url(r'^latest/feed/$', LatestEntriesFeed()),
)
