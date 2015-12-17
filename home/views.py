import json

from datetime import datetime
from django import http
from lib import feedparser
from twitter import Twitter, OAuth


def home(request):
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

	upcoming = "<h3>Upcoming Contests</h3><table>" + "<tr><th>Contest Title</th><th>Start Date</th><th>End Date</th></tr>"
	active = "<h3>Active Contests</h3><table>" + "<tr><th>Contest Title</th><th>Start Date</th><th>End Date</th></tr>"
	for feed in reversed(feeds['entries']):
		if datetime.strptime(feed['starttime'],"%Y-%m-%d %H:%M:%S UTC") > nowDate:
			upcoming += '<tr><td><a href = "' + feed['url'] + '">' + feed['title'] + '</a></td><td>' + feed['starttime'] + '</td><td>' + feed['endtime'] + '</td></tr>'
		if datetime.strptime(feed['starttime'],"%Y-%m-%d %H:%M:%S UTC") <= nowDate and datetime.strptime(feed['endtime'],"%Y-%m-%d %H:%M:%S UTC") >= nowDate:
 			active += '<tr><td><a href = "' + feed['url'] + '">' + feed['title'] + '</a></td><td>' + feed['starttime'] + '</td><td>' + feed['endtime'] + '</td></tr>'
	upcoming += "</table>"
	active += "</table>"
	s = s + active + upcoming + tweets + msj

	return http.HttpResponse(s)
