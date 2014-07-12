# vim: et ts=4 sw=4
from django.conf.urls import patterns, url

from reader.views import IndexView#, PostList
from reader.ajaxviews import JSONFeedList, JSONPostList, MarkPost
#from django.views.generic import TemplateView

urlpatterns = patterns('',
        #url(r'', include('feincms.urls')),
        #url(r'^$', TemplateView.as_view(template_name="reader/index.html")),

        url(r'^$', IndexView.as_view()),
        url(r'^page/(?P<page>\d+)$', IndexView.as_view()),
        url(r'^feed/(?P<feed>\d+)$', IndexView.as_view()),
        url(r'^feed/(?P<feed>\d+)/page/(?P<page>\d+)$', IndexView.as_view()),
        url(r'^category/(?P<category>\d+)$', IndexView.as_view()),
        url(r'^category/(?P<category>\d+)/page/(?P<page>\d+)$', IndexView.as_view()),

        url(r'^ajax/markpost/read/(?P<read>\d+)$', MarkPost.as_view()),
        url(r'^ajax/markpost/starred/(?P<starred>\d+)', MarkPost.as_view()),
        url(r'^ajaxfeedlist$', JSONFeedList.as_view()),
        url(r'^ajaxpostlist$', JSONPostList.as_view()),
        #url(r'^postlist$', PostList.as_view()),
        )
