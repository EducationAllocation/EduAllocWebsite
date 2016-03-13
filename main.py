'''
Created on Nov 14, 2015

@author: Andrew
'''
import webapp2
import os
from google.appengine.ext.webapp import template
class DonateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        path = os.path.join(os.path.dirname(__file__),'donate.html')
        self.response.out.write(template.render(path,template_values))
class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        path = os.path.join(os.path.dirname(__file__),'contact.html')
        self.response.out.write(template.render(path,template_values))
class StaffHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        path = os.path.join(os.path.dirname(__file__), 'staff.html')
        self.response.out.write(template.render(path, template_values))
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        path = os.path.join(os.path.dirname(__file__), 'main.html')
        self.response.out.write(template.render(path, template_values))
app = webapp2.WSGIApplication([ 
    ('/donate', DonateHandler),
    ('/contact', ContactHandler),                                     
    ('/staff', StaffHandler),
    ('/.*', MainHandler),
    
], debug=True)