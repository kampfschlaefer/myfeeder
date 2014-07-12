# - encoding: utf8 -
# vim: et sw=4

from django_extensions.management.jobs import HourlyJob
from reader.importfeeds import parsefeed
from reader import models as reader

class Job(HourlyJob):
    help = "Fetch the feeds."

    def execute(self):
        for f in reader.Feed.objects.all():
            parsefeed(f)

