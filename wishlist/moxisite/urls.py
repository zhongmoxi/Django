from django.conf.urls import patterns, include, url
from django.conf import settings
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
    # url(r'^hello/$', 'moxisite.views.hello'),
    # url(r'^search-form/$', views.search_form),
    # url(r'^search/$', views.search),
    url(r'^add_entry/$', 'blog.views.add_entry'),
    #url(r'^entry/(?P<entry_id>\d+)$', 'blog.views.entry'),
    url(r'^show_wishes/$', 'blog.views.show_entries'),
    url(r'^wish/(?P<wish_id>\d+)/edit/$', 'blog.views.edit_wish', name='edit-wish'),
    url(r'^wish/(?P<wish_id>\d+)/delete/$', 'blog.views.delete_wish'),
    url(r'^wish/(?P<wish_id>\d+)$', 'blog.views.wish'),
    url(r'^$', 'blog.views.show_wishes', name='home'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^logout/$', 'blog.views.logout'),
    url(r'^accounts/login/$', 'blog.views.login'),
    url(r'^register/$', 'blog.views.register'),
    url(r'^latest/feed/$', LatestEntriesFeed()),
    url(r'^user/(?P<user_id>\d+)$', 'blog.views.user_wishes'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
)
