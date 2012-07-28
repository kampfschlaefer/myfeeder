# vim: et ts=4 sw=4

from django.contrib import admin
from reader.models import *

class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category']
    list_filter = ['category']
    pass

class EnclosureInlineAdmin(admin.StackedInline):
    model = Enclosure
    extra = 0


class PostingAdmin(admin.ModelAdmin):
    list_display = ['feed', 'title', 'publishdate']
    list_display_links = ['title', ]
    list_filter = ['feed', 'author', 'feed__category']
    ordering = ['publishdate', 'feed']

    inlines = [ EnclosureInlineAdmin, ]

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ['posting', 'etype', 'length', 'href']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

admin.site.register(Feed, FeedAdmin)
admin.site.register(Posting, PostingAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
admin.site.register(Category, CategoryAdmin)

