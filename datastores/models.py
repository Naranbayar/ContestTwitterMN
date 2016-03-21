import datetime
from google.appengine.ext import db
#from google.appengine.api import users


class Contest(db.Model):
	title = db.StringProperty(required=True)
	contest_type = db.StringProperty(required=True, choices=set(["online", "onsite"]))
	contest_start_date = db.DateProperty()
	contest_end_date = db.DateProperty()
	approved_contest = db.BooleanProperty(required=True)
	detail = db.StringProperty()
