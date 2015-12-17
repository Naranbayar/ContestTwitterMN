# Run tests with "manage.py test".

from google.appengine.api import users
from __future__ import unicode_literals
from django import http
from django.test import TestCase
from . import views
import webapp2

class HomeViewTest(TestCase):
    def test_home(self):
        requst = http.HttpRequest()
        response = views.home(request)
        self.response.headers['Content-Type'] = "text/html; charset=utf-8"
        self.assertEqual(200, response.status_code)
        self.assertIn('Hello World!', response.content)
