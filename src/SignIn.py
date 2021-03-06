""" ********** """
""" * IMPORT * """
""" ********** """
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SignIn(webapp2.RequestHandler):

    def get(self):

        """ ************* """
        """ * MAIN MENU * """
        """ ************* """
        template = JINJA_ENVIRONMENT.get_template('SignIn.html')
        self.response.write(template.render())

