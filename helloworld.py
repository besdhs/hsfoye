from google.appengine.api import urlfetch
from google.appengine.ext import webapp, ndb
from google.appengine.ext.key_range import simplejson
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
from resource import Resource

KEY_RESOURCES = "Resources"
KEY_MIDDLESCHOOL = "6 - 8"
KEY_HIGHSCHOOL = "9 - 12"
KEY_COLLEGE = "College"
KEY_ALUMNI = "Alumni"



# class Resource(ndb.Model):
#     name = ndb.StringProperty()
#     website = ndb.StringProperty()
#     overview = ndb.StringProperty()
#     audience = ndb.StringProperty()
#     content = ndb.IntegerProperty()
#     presentation = ndb.IntegerProperty()
#     spanish = ndb.BooleanProperty()
#     notes = ndb.StringProperty(repeated=True)
#     license = ndb.StringProperty()
#     grade = ndb.StringProperty()

class BuildDB(webapp.RequestHandler):
 
    @classmethod 
    def build(cls):
        #Need admin acc to import
        url = "https://spreadsheets.google.com/feeds/list/0ApN6pOTp7qkZdDVDMW1YSEZUelV2TFUwcFpzblM4cnc/od6/public/values?alt=json"
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            feed_obj = simplejson.loads(result.content)
            if "feed" in feed_obj:
                entries = feed_obj["feed"]["entry"]
                # Make an application entity for each entry in feed
                last = {}
#                 cls.response.out.write('<html><body>')
                for entry in entries:
                    name = entry["gsx$name"]['$t']
#                     self.response.out.write("<p>" + name + "</p>");
                    note = entry["gsx$notes"]['$t']
                    # If new name
                    if not name in last.keys():
                        res = Resource()
                        res.name = name
                        res.note = []
                        logging.debug("Resource repeated %s", name)
                        res.website = entry["gsx$website"]['$t']
                        res.overview = entry["gsx$overview"]['$t']
                        res.audience = entry["gsx$audience"]['$t']
                        content = entry["gsx$content"]['$t']
                        if len(content) == 0:
                            res.content = 0
                        else:
                            res.content = int(content)
                        presentation = entry["gsx$presentation"]['$t']
                        if len(presentation) == 0:
                            res.presentation = 0
                        else:
                            res.presentation = int(presentation)
                        spanish = entry["gsx$spanish"]['$t']
                        if spanish == "No":
                            res.spanish = False
                        else :
                            res.spanish = True
                        res.license = entry["gsx$license"]['$t']
                        res.grade = entry["gsx$grade"]['$t']
                    else:
                        res = last[name] # Resource
                        res.notes.append(note)
                        logging.debug("New resource found %s", name)
                    res.put()
                    last[name] = res
                resources = Resource.getResources()
                i = 0
                for res in resources:
#                     self.response.out.write("<p>" + str(res.name) + "</p>");
                    i = i + 1
                    #print ("<p>" + str(res) + "</p>")
#                 cls.response.out.write('Num Resources ' + str(i))   
#                 cls.response.out.write('</body></html>')
#          self.response.headers['Content-Type'] = 'text/plain'
#                     self.response.out.write('<html><body>')
#                     self.response.out.write("<p>" + " " + name +  website + overview + audience + content + presentation + spanish + notes + link_license + grade)   
#                     self.response.out.write('</body></html>')
 
# application = webapp.WSGIApplication([('/', MainPage)], debug=True)
#  
# def main():
#     run_wsgi_app(application)
#  
# if __name__ == "__main__":
#     main()