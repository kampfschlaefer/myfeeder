# vim: et ts=4 sw=4

from django.contrib import admin
from reader.models import *

class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    pass

class PostingAdmin(admin.ModelAdmin):
    list_display = ['feed', 'title', 'publishdate']
    list_display_links = ['title', ]
    list_filter = ['feed', 'author']
    ordering = ['publishdate', 'feed']
    pass

admin.site.register(Feed, FeedAdmin)
admin.site.register(Posting, PostingAdmin)

