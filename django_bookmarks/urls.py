from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks.views import *
from django.views.generic import TemplateView
from social.views import *
from blog.views import *
from project1.views import *
from soc.views import *
from genviews.views import MyViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
                       url(r'^aj_req/$', main_page),
                       #  ( r'^$', main_page2),
                       #  (r'^search/', search_req)
                       #  Examples:
                       #  url(r'^$','django_bookmarks.views.home',name='home'),
                       #  url(r'^blog/', include('blog.urls')),
                       # ,url(r'^form/',input_req)
                       # ,url(r'^blog/$',blog_req)
                       # ,url(r'^blog/input/$',blog_input)
                       # ,url(r'^blog/view/$',blog_showdata)
                       url(r'^project1/check_msg$', check_msg),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^project1/$', check_register, name='testpge'),
                       url(r'^project1/logout/$', log_user_out),
                       url(r'^project1/(\d+)$', message_user, name='msg_snd'),
                       url(r'^project1/(\d*)/aj_req$', aj_req),
                       url(r'^sock_(\w+)/$', sock),
                       url(r'^project1/ang_req$', ang_msg),
                       url(r'^gen_views/$', login_required(TemplateView.as_view(template_name='gen_template.html'))),
                       )
urlpatterns += static(settings.FONT_URL, document_root=settings.FONT_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
