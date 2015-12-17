# appcfg.py -A contestmn update ContestTwitterMN/
# dev_appserver.py ContestTwitterMN/

from django import http
# import tweepy
import feedparser
from datetime import datetime
from twitter import *
import json

def home(request):
	# auth = tweepy.OAuthHandler("0I87DLCvIvIs8r6fD3iiYaWQv", "FExCvaLZHdHMmtudeFJzgCIf7z94AZG7Zh0gJru3gQDaYlqgcQ")
	# auth.set_access_token("3219043802-lbrCq80T6NMW5iesaz7rYr7gyWBF1uatbHhBqPM", "BXlVJAHXMdfSPeqMYFh0toPinCh4D4SJcnMpvv1CmIAZe")

	# api = tweepy.API(auth)

	# public_tweets = api.home_timeline()

	# tweets = ""
	# for tweet in public_tweets:
	# 	tweets = tweets + tweet.text

	# api.update_status(status="Hello World!!! It's first tweet from my django app test")
	t = Twitter(auth=OAuth("3219043802-lbrCq80T6NMW5iesaz7rYr7gyWBF1uatbHhBqPM", 
							"BXlVJAHXMdfSPeqMYFh0toPinCh4D4SJcnMpvv1CmIAZe", 
							"0I87DLCvIvIs8r6fD3iiYaWQv", 
							"FExCvaLZHdHMmtudeFJzgCIf7z94AZG7Zh0gJru3gQDaYlqgcQ"))

	# Get your "home" timeline
	public_tweets = t.statuses.user_timeline(screen_name="NaranbayarU",count=5)
	# t.statuses.update(status="First tweet from twitter library")
	tweets = "<h2>My last 5 tweets</h2><ul>"
	for tweet in public_tweets:
		tweets += '<li><a href="https://twitter.com/NaranbayarU/status/' + tweet['id_str'] + '">' + tweet['text'] + '</a></li>'
	tweets += '</ul>'

	msj = '<center><h1>Tweet about upcoming programming contests from hackerrank calendar. Coming Soon!!!</h1></center>'
	rss_url = "http://www.hackerrank.com/calendar/feed.rss"
	feeds = feedparser.parse( rss_url )
	nowDate = datetime.utcnow()
	s = "<h2>Current time is : " + nowDate.strftime("%Y-%m-%d %H:%M:%S UTC") + "</h2><br>"

	t = "<table>" + "<tr><th>Contest Title</th><th>Start Date</th><th>End Date</th></tr>"
	for feed in reversed(feeds['entries']):
		if datetime.strptime(feed['starttime'],"%Y-%m-%d %H:%M:%S UTC") > nowDate:
			# api.update_status(feed['title'] + " will begin soooon")
			# break
			t += '<tr><td><a href = "' + feed['url'] + '">' + feed['title'] + '</a></td><td>' + feed['starttime'] + '</td><td>' + feed['endtime'] + '</td></tr>'
	t += "</table>"
	s = s + t + tweets + msj

	return http.HttpResponse(s)