myfeeder
========

After google decided to [focus on its core project](http://xkcd.com/1361/) and shut down the reader, I seeked a replacement. While I found [selfoss](https://github.com/SSilence/selfoss), I also set out to write my own RSS-reader. Given my notorious lack of time, this is actually quite good...

# Installation

Given a linux-shell, git and python:

- Clone from github: `git clone <cloneurl>`
- cd into myfeeder: `cd myfeeder`
- create a virtual environment: `virtualenv .`
- activate the virtual environment: `. bin/activate`
- install requirements: `pip install -r requirements.txt`
- initialize the db: `python manage.py syncdb --migrate`
- create a first superuser: `python manage.py createsuperuser`
- run the webserver: `python manage.py runserver`
- start your browser and access the webserver as shown in the output from above and append 'reader/' to the url
- click on the admin-link to log in as your admin-user and add feeds.
- run the cron-job on the commandline to fetch the feeds: `python manage.py runjobs hourly`

Seems a bit complicated. But its not finished. And its only for me so I don't forget till the next time...