import json
from datetime import datetime

from django.conf import settings
from django.shortcuts import render

from lib import feedparser
from twitter import Twitter, OAuth


def home(request):
    utcnow = datetime.utcnow()
    datetime_format = '%Y-%m-%d %H:%M:%S UTC'
    hackerrank_url = 'http://www.hackerrank.com/calendar/feed.rss'

    # Tweets
    twitter = Twitter(auth=OAuth(settings.TOKEN,
                                 settings.TOKEN_KEY,
                                 settings.SECRET,
                                 settings.SECRET_KEY))

    tweets = twitter.statuses.user_timeline(screen_name='NaranbayarU', count=5)

    # Contests
    active_contests, upcoming_contests = [], []
    feeds = feedparser.parse(hackerrank_url)
    for feed in reversed(feeds['entries']):
        start_time = datetime.strptime(feed['starttime'], datetime_format)
        end_time = datetime.strptime(feed['endtime'], datetime_format)

        # Active contests
        if start_time <= utcnow <= end_time:
            active_contests.append({
                'url': feed['url'],
                'title': feed['title'],
                'start_time': feed['starttime'],
                'end_time': feed['endtime'],
            })

        # Upcoming contests
        if start_time > utcnow:
            upcoming_contests.append({
                'url': feed['url'],
                'title': feed['title'],
                'start_time': feed['starttime'],
                'end_time': feed['endtime'],
            })

    return render(request, 'index.html', {
        'current_time': utcnow.strftime('%Y-%m-%d %H:%M:%S UTC'),
        'active_contests': active_contests,
        'upcoming_contests': upcoming_contests,
        'tweets': tweets,
    })
