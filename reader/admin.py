# vim: et ts=4 sw=4

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reader.models import Feed, Posting, Enclosure, PostMark, Category

class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category']
    list_filter = ['category']
    pass

class EnclosureInlineAdmin(admin.StackedInline):
    model = Enclosure
    extra = 0

class MarkInlineAdmin(admin.TabularInline):
    model = PostMark
    extra = 1


class PostingAdmin(admin.ModelAdmin):
    list_display = ['feed', 'title', 'publishdate', 'isread', 'isstarred']
    list_display_links = ['title', ]
    list_filter = ['feed', 'author', 'feed__category', 'marks__mark' ]
    ordering = ['publishdate', 'feed']

    inlines = [ EnclosureInlineAdmin, MarkInlineAdmin ]

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ['posting', 'etype', 'length', 'href']

class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'parent']

admin.site.register(Feed, FeedAdmin)
admin.site.register(Posting, PostingAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
admin.site.register(Category, CategoryAdmin)