import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

class Login(webapp2.RequestHandler):
    
    print "hello"
    