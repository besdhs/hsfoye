from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi
import webapp2
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
#         self.response.write(MAIN_PAGE_HTML)
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "HSF Oye",
            "urls": [],
            "curr_url": self.request.url,
            "college_url": self.request.url + "college",
            "high_url": self.request.url + "college",
            "middle_url": self.request.url + "college",
            "alumni_url": self.request.url + "college",
        }
        self.response.out.write(template.render('html/index.html', values))
        
class CollegeTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.write('<html><body>College')
#         self.response.write(self.request.get('first') + self.request.get('last'))
        self.response.write('</body></html>') 
        
class HighSchoolTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.write('<html><body>HighSchool')
#         self.response.write(self.request.get('first') + self.request.get('last'))
        self.response.write('</body></html>') 
        
class MiddleTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.write('<html><body>Middle School')
#         self.response.write(self.request.get('first') + self.request.get('last'))
        self.response.write('</body></html>') 
        
class AlumniTypePage(webapp2.RedirectHandler):
    
    def get(self):
        self.response.write('<html><body>Alumni')
#         self.response.write(self.request.get('first') + self.request.get('last'))
        self.response.write('</body></html>')         

application = webapp2.WSGIApplication([('/', MainPage),
                                      ('/college', CollegeTypePage),
                                      ('/college', HighSchoolTypePage),
                                      ('/college', AlumniTypePage),], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()