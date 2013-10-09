from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','guestbook.views.guestbookdetails'),
    url(r'^get/(?P<guestbook_id>\d+)/$','guestbook.views.guestbook'),
    url(r'^create/$','guestbook.views.create'),
    url(r'^success/$','guestbook.views.success'),
)
