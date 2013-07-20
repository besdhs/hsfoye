from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi
import webapp2
from helloworld import BuildDB
from resource import Resource
#from google.appengine.api import users

resource_types = {
    '/6-8': 'Resources on Grades 6-8',
    '/9-12': 'Resources on Grades 9-12',
    '/college': 'Resources on College',
    '/alumni': 'Resources on Alumni',
}

MAIN_PAGE_HTML = """\
<form action="/on_add_person" method="get">
                  <div>first:<input type="text" name="first"></div> 
                  <div>last:<input type="text" name="last"></div>    
                  <div><input type="submit" value="Add Person"></div>
                </form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #BuildDB.build()
#         self.response.write(MAIN_PAGE_HTML)
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "HSF Oye",
            "urls": [],
            "curr_url": self.request.url,
            "college_url": self.request.url + "college",
            "high_url": self.request.url + "highschool",
            "middle_url": self.request.url + "middle",
            "alumni_url": self.request.url + "alumni",
        }
        self.response.out.write(template.render('html/index.html', values))
        
class CollegeTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "College",
            "scholarship": self.request.url + "/scholarship",
            "curr_url": self.request.url,
        }
        self.response.out.write(template.render('html/college.html', values))
        
class HighSchoolTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "High School",
            "curr_url": self.request.url,
        }
        self.response.out.write(template.render('html/highschool.html', values))
        
class MiddleTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "Middle School",
            "curr_url": self.request.url,
        }
        self.response.out.write(template.render('html/middle.html', values))
        
class AlumniTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "Alumni",
            "curr_url": self.request.url,
        }
        self.response.out.write(template.render('html/alumni.html', values))    

class CollegeScholarship(webapp2.RedirectHandler): 
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        resources = Resource.getResourcesForCollege()
        values = {
            "resources" : resources,
            "scholarship": self.request.url,
            "curr_url": self.request.url,
        }
        self.response.out.write(template.render('html/cship.html', values))          

application = webapp2.WSGIApplication([('/', MainPage),
                                      ('/college', CollegeTypePage),
                                      ('/highschool', HighSchoolTypePage),
                                      ('/alumni', AlumniTypePage),
                                      ('/middle', MiddleTypePage),
                                      ('/college', CollegeTypePage),
                                      ('/college/scholarship', CollegeScholarship),], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()