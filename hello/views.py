# appcfg.py -A contestmn update ContestTwitterMN/
# dev_appserver.py ContestTwitterMN/

from django import http
#import tweepy
#import json 
import feedparser
from datetime import datetime

def home(request):
#	auth = tweepy.OAuthHandler("0I87DLCvIvIs8r6fD3iiYaWQv", "FExCvaLZHdHMmtudeFJzgCIf7z94AZG7Zh0gJru3gQDaYlqgcQ")
#	auth.set_access_token("3219043802-lbrCq80T6NMW5iesaz7rYr7gyWBF1uatbHhBqPM", "BXlVJAHXMdfSPeqMYFh0toPinCh4D4SJcnMpvv1CmIAZe")


#	api = tweepy.API(auth)

	# public_tweets = api.home_timeline()

	# s = ""
	# for tweet in public_tweets:
	# 	s = s + tweet.text

	# api.update_status(status="Hello World!!!")

	rss_url = "http://www.hackerrank.com/calendar/feed.rss"
	feeds = feedparser.parse( rss_url )
	nowDate = datetime.utcnow()

	s = " Time is : " + nowDate.strftime("%Y-%m-%d %H:%M:%S UTC") + "<br>" + "<ul>"
	for feed in feeds['entries']:
		if datetime.strptime(feed['starttime'],"%Y-%m-%d %H:%M:%S UTC") > nowDate:
			# api.update_status(feed['title'] + " will begin soooon")
			# break
			s = s + '<li>' + feed['title'] + ' ' + feed['starttime'] + ' ' + feed['endtime'] + '</li>'
	s = s + "</ul>"
	
	return http.HttpResponse(s)