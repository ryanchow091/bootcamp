from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'bootcamp.core.views.home', name='home'),
    url(r'^login/$', 'bootcamp.auth.views.login', name='login'),
    url(r'^logout/$', 'bootcamp.auth.views.logout', name='logout'),
    url(r'^signup/$', 'bootcamp.auth.views.signup', name='signup'),
    url(r'^settings/$', 'bootcamp.core.views.settings', name='settings'),
    url(r'^settings/picture/$', 'bootcamp.core.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'bootcamp.core.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'bootcamp.core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'bootcamp.core.views.password', name='password'),
    url(r'^network/$', 'bootcamp.core.views.network', name='network'),
    url(r'^feeds/', include('bootcamp.feeds.urls')),
    url(r'^questions/', include('bootcamp.questions.urls')),
    url(r'^articles/', include('bootcamp.articles.urls')),
    url(r'^(?P<username>[^/]+)/$', 'bootcamp.core.views.profile', name='profile'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)