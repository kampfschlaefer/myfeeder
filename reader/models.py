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

    def __unicode__(self):
        return self.title

class Enclosures(models.Model):
    posting = models.ForeignKey('Posting')
    etype = models.CharField(max_length=200)
    length = models.IntegerField(default=-1)
    href = models.URLField(blank=False)

