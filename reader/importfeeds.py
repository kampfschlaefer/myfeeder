#!/usr/bin/env python
# - encoding: utf8 -
# vim: et sw=4

import os, sys, datetime
os.environ['DJANGO_SETTINGS_MODULE']='myfeeder.settings'

sys.path.insert(0, '.')
#print sys.path

from reader.models import *
from django.db import connection, transaction, utils
import feedparser, pytz, zlib

def parsefeed(feed):
    if isinstance(feed, str):
        f = Feed.objects.get(url=feed)
    if isinstance(feed, int):
        f = Feed.objects.get(pk=feed)
    if isinstance(feed, Feed):
        f = feed
    #else:
    #    f = Feed.objects.get(feed)
    print f

    print f.url
    feed = feedparser.parse(f.url)

    print feed.keys()
    if len(feed.entries) > 0:
        print feed.entries[0].keys()
    print feed.entries[:2]

    newentries = 0
    for entry in feed.entries:
        try:
            origid = entry.id
        except AttributeError:
            origid = zlib.adler32(entry.link)
        if Posting.objects.filter(feed__pk=f.id, origid=origid).count() == 0:
            try:
                author = entry.author
            except AttributeError:
                author = None
            p = Posting(feed=f, origid=origid, title=entry.title, content=entry.summary, link=entry.link, author=author)
            try:
                t = entry.updated_parsed
            except AttributeError:
                t = feed.updated_parsed
            p.publishdate = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, 0, pytz.utc)
            p.save()
            newentries += 1
    print "Imported {} new entries from {}".format(newentries, f)


if __name__ == '__main__':

    #parsefeed('https://development.bcs.bcs/trac/bcspackages/timeline?ticket=on&changeset=on&milestone=on&wiki=on&max=50&author=&daysback=90&format=rss')

    for f in Feed.objects.all().values_list('id'):
        #print f[0]
        parsefeed(f[0])

