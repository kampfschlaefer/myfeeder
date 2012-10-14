# vim: et ts=4 sw=4
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime, re

# Create your models here.

class Posting(models.Model):
    feed = models.ForeignKey('Feed')
    origid = models.CharField(max_length=250,blank=True)
    title = models.CharField(max_length=250)
    link = models.URLField(blank=True)
    content = models.TextField()
    author = models.CharField(max_length=250, blank=True)
    publishdate = models.DateTimeField(default=datetime.datetime.now())

    def isread(self):
        return (self.marks.filter(mark='READ').count() > 0)
    def isstarred(self):
        return (self.marks.filter(mark='STAR').count() > 0)

    def displaywide(self):
        if self.feed.wide_allowed and not self.isread() and (len(re.sub('<[^>]+>', '', self.content)) > 100 or re.search('<img [^>]+>', self.content)):
            return True
        return False

class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250)
    category = TreeForeignKey('Category', related_name="feeds", blank=True, null=True)
    wide_allowed = models.BooleanField(default=False, verbose_name="Allow big posts to display big")

    def __unicode__(self):
        return self.title

    def unread(self):
        #print "Feed ({}).unread will give {}.".format(self, len(filter(lambda p: not p.isread(), self.posting_set.all())))
        print "Feed ({}).unread will give {}.".format(self, self.posting_set.filter(~models.Q(marks__mark='READ')).count())
        #return len(filter(lambda p: not p.isread(), self.posting_set.all()))
        return self.posting_set.filter(~models.Q(marks__mark='READ')).count()

class Enclosure(models.Model):
    posting = models.ForeignKey('Posting', related_name='enclosures')
    etype = models.CharField(max_length=200)
    length = models.IntegerField(default=-1)
    href = models.URLField(blank=False)

class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='subcategories')

    class MPTTMeta:
        order_insertion_by = 'title'

    def __unicode__(self):
        return self.title

    def getfeeds(self):
        """ Return the feeds that are direct or indirect childs of this category. """
        feedlist = [ f for f in self.feeds.all() ]
        for c in self.subcategories.all():
            feedlist += [ f for f in c.getfeeds() ]

        return feedlist

    def unread(self):
        u = 0
        for c in self.get_children():
            #print "Getting unread for ", c
            u += c.unread()
        for f in self.feeds.all():
            u += f.unread()
        #print " u is now ", u
        return u

class PostMark(models.Model):
    posting = models.ForeignKey(Posting, related_name='marks')
    MARKS = (
            ('READ', 'Read'),
            ('STAR', 'Starred'),
            )
    mark = models.CharField(max_length=5, choices=MARKS)

