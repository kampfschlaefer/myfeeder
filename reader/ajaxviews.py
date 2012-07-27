# vim: et ts=4 sw=4

from django import http
#from django.utils import simplejson as json
import json, datetime
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
            return JSONEncoder.default(self, obj)

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
        print context
        return json.dumps(context, cls=JSONDateTimeEncoder)

class JSONFeedList(JSONResponseMixin, BaseListView):
    queryset = Feed.objects.all().values()
    pass
