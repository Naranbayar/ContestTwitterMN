import datetime
from google.appengine.ext import db


class Contest(db.Model):
	title = db.StringProperty(required=True)
	contest_type = db.StringProperty(required=True, choices=set(["online", "onsite"]))
	contest_start_date = db.DateProperty()
	contest_end_date = db.DateProperty()
	approved_contest = db.BooleanProperty(required=True)
	detail = db.StringProperty()
