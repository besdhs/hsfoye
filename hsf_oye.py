from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.api import users
from google.appengine.ext.webapp import template

resource_types = {
    '/6-8': 'Resources on Grades 6-8',
    '/9-12': 'Resources on Grades 9-12',
    '/college': 'Resources on College',
    '/alumni': 'Resources on Alumni',
}
class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        values = {
            "title": "Main Page",
            "urls": [],
        }
        self.response.out.write(template.render('html/index.html', values))
        

class ResourceTypePage(webapp.RequestHandler):
    
application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()