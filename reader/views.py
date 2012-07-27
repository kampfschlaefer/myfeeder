# vim: et ts=4 sw=4
# Create your views here.

from django.views.generic.list import ListView
from django.views.generic import TemplateView
from reader import models

class PostList(ListView):

    #queryset = models.Posting.objects.all()
    model = models.Posting

    def get_context_data(self, **kwargs):
        ret = kwargs
        ret['pagetitle'] = 'All Postings'
        return ret

class IndexView(TemplateView):

    template_name = "reader/index.html"

    def get_context_data(self, **kwargs):
        print kwargs.update({'pagetitle': 'My feed reader', })
        return kwargs.update({'pagetitle': 'My feed reader', })

