# vim: et ts=4 sw=4
# Create your views here.

from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.db.models import Q
from reader.models import *

class PostListMixin:
    def get_postlist(self, category=None, feed=None):
        q = Q()
        if category is not None:
            q = Q(feed__in=Category.objects.get(pk=int(category)).getfeeds())
        if feed is not None:
            q = Q(feed__pk=int(feed))
        queryset = Posting.objects.filter(q).order_by('-publishdate')
        return queryset

#class PostList(ListView):
#
#    #queryset = models.Posting.objects.all()
#    model = Posting
#
#    def get_context_data(self, **kwargs):
#        ret = kwargs
#        ret['pagetitle'] = 'All Postings'
#        return ret

class IndexView(TemplateView, PostListMixin):

    template_name = "reader/index.html"

    def get_context_data(self, **kwargs):
        #print "IndexView.get_context_data(", kwargs, ")"
        postsperpage = 50
        category = None
        feed = None
        page = 1
        nextpagelink = '/reader'
        if kwargs.has_key('category'):
            category = int(kwargs['category'])
            nextpagelink += '/category/{}'.format(category)
        if kwargs.has_key('feed'):
            feed = int(kwargs['feed'])
            nextpagelink += '/feed/{}'.format(feed)
        if kwargs.has_key('page'):
            page = int(kwargs['page'])
        previouspagelink = ''
        if page > 1:
            previouspagelink = '{}/page/{}'.format(nextpagelink, page-1)
        nextpagelink += '/page/{}'.format(page+1)
        postlist = self.get_postlist(category=category, feed=feed)[(page-1)*postsperpage:page*postsperpage]
        #print [ p.displaywide() for p in postlist ]
        return {
                'pagetitle': 'My feed reader',
                'postlist': postlist,
                'page': page,
                'nextpagelink': nextpagelink,
                'previouspagelink': previouspagelink,
                'categories': Category.objects.all(),
                }

