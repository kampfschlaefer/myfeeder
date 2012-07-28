# vim: et ts=4 sw=4
from django.db import models
import datetime

# Create your models here.

class Posting(models.Model):
    feed = models.ForeignKey('Feed')
    origid = models.CharField(max_length=250,blank=True)
    title = models.CharField(max_length=250)
    link = models.URLField(blank=True)
    content = models.TextField()
    author = models.CharField(max_length=250, blank=True)
    publishdate = models.DateTimeField(default=datetime.datetime.now())

class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250)
    category = models.ForeignKey('Category', related_name="feeds", blank=True, null=True)

    def __unicode__(self):
        return self.title

class Enclosure(models.Model):
    posting = models.ForeignKey('Posting', related_name='enclosures')
    etype = models.CharField(max_length=200)
    length = models.IntegerField(default=-1)
    href = models.URLField(blank=False)

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', blank=True, null=True, related_name='subcategories')

    def __unicode__(self):
        return self.title

    def getfeeds(self):
        """ Return the feeds that are direct or indirect childs of this category. """
        feedlist = [ f for f in self.feeds.all() ]
        for c in self.subcategories.all():
            feedlist += [ f for f in c.getfeeds() ]

        return feedlist

class PostMark(models.Model):
    posting = models.ForeignKey(Posting, related_name='marks')
    MARKS = (
            ('READ', 'Read'),
            ('STAR', 'Starred'),
            )
    mark = models.CharField(max_length=5, choices=MARKS)

