# vim: et ts=4 sw=4

from django import http
#from django.utils import simplejson as json
import json, datetime, re
from django.db.models import Q
from django.views.generic.list import BaseListView
from django.views.generic.base import View
from reader.models import *

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            try:
                iterable = iter(obj)
            except TypeError:
                pass
            else:
                return list(iterable)
            return json.JSONEncoder.default(self, obj)

class JSONTimeStampEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return calendar.timegm(obj.timetuple())*1000
        else:
            try:
                iterable = iter(obj)
            except TypeError:
                pass
            else:
                return list(iterable)
            return json.JSONEncoder.default(self, obj)


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
            content_type='application/json',
            **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        #print context
        return json.dumps(context, cls=JSONDateTimeEncoder)

class JSONFeedList(JSONResponseMixin, View):

    def categoriestolist(self, cats):
        ret = []
        for c in cats:
            r = {'id': c.id, 'title': c.title}
            childs = self.categoriestolist(Category.objects.filter(parent=c.id))
            r['childs'] = childs

    def buildcategoriestree(self, catid, includefeeds=True):
        ret = []
        for c in Category.objects.filter(parent=catid):
            r = {'id': c.id, 'title': c.title, 'type': 'category'}
            childs = self.buildcategoriestree(c.id)
            if len(childs) > 0:
                r['childs'] = childs
            ret.append(r)
        for f in Feed.objects.filter(category=catid):
            r = {'id': f.id, 'title': f.title, 'type': 'feed'}
            ret.append(r)
        return ret

    def get(self, request, *args, **kwargs):
        #print "Called get()"
        l = self.buildcategoriestree(None)
        #print l

        return self.render_to_response(l)

    pass

class JSONPostList(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        #print request.GET
        #print args
        #print kwargs
        queryset = None
        q = Q()
        if request.GET.has_key('type') and request.GET.has_key('id'):
            t = request.GET['type']
            i = request.GET['id']
            if t == 'category':
                cat = Category.objects.get(pk=i)
                feeds = cat.getfeeds()
                q = Q(feed__in=feeds)
            if t == 'feed':
                q = Q(feed__pk=i)
        queryset = Posting.objects.filter(q).order_by('-publishdate')[:20]#.values()#'id', 'title', 'link', 'content', 'author', 'publishdate', 'enclosures')
        ret = []
        for p in queryset:
            tmp = {}
            tmp['content'] = re.sub('(class|div)', 'x\\1', p.serializable_value('content'))
            for field in ('id', 'title', 'link', 'author', 'publishdate'):
                tmp[field] = p.serializable_value(field)
            for call in ('isread', 'isstarred'):
                tmp[call] = eval('p.%s()' % call)
            #for m in p.marks.all():
            tmp['marks'] = p.marks.count()
            ret.append(tmp)
        #print "queryset: ", queryset[:1]
        #print "ret: ", ret[:2]

        return self.render_to_response(ret)#queryset)

class MarkPost(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        print "MarkPost.get(", args, kwargs, ")"
        postread = None
        poststarred = None
        ret = {}
        if kwargs.has_key('read'):
            postread = int(kwargs['read'])
        if kwargs.has_key('starred'):
            poststarred = int(kwargs['read'])
        if postread is not None:
            #Posting.objects.get(pk=postread).marks.add('READ')
            PostMark(posting_id=postread, mark='READ').save()
            ret['read'] = postread

        return self.render_to_response(ret)

