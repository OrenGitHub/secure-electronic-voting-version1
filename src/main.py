""" ****************** """
""" * GENERAL IMPORT * """
""" ****************** """
import os
import urllib

""" ****************** """
""" * GENERAL IMPORT * """
""" ****************** """
from google.appengine.api import users
from google.appengine.ext import ndb

""" ****************** """
""" * GENERAL IMPORT * """
""" ****************** """
import jinja2
import webapp2

""" ****************** """
""" * PROJECT IMPORT * """
""" ****************** """
from Login import Login
from SignIn import SignIn

""" ********** """
""" * JINJA! * """
""" ********** """
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
""" ************ """
""" * MainPage * """
""" ************ """
class MainPage(webapp2.RequestHandler):

    def get(self):

        """ ************* """
        """ * MAIN MENU * """
        """ ************* """
        template = JINJA_ENVIRONMENT.get_template('MainPage.html')
        self.response.write(template.render())
        """ """
                                            

""" ****************** """
""" * URL To Classes * """
""" ****************** """
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/SignIn', SignIn),
    ('/Login', Login),
    ('/SeeADemo', SeeADemo)    
], debug=True)

