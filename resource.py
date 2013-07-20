'''
Created on Jul 19, 2013

@author: mhotan
'''
from google.appengine.ext import ndb

GRADE6_8 = "6 - 8"
GRADE9_12 = "9 - 12"
COLLEGE = "College"
ALUMNI = "Alumni"

class Resource(ndb.Model):
    '''
    classdocs
    '''
    name = ndb.StringProperty()
    website = ndb.StringProperty()
    overview = ndb.StringProperty()
    audience = ndb.StringProperty()
    content = ndb.IntegerProperty()
    presentation = ndb.IntegerProperty()
    spanish = ndb.BooleanProperty()
    notes = ndb.StringProperty(repeated=True)
    license = ndb.StringProperty()
    grade = ndb.StringProperty()

    @classmethod
    def getResources(cls):
        return cls.query()
        
    @classmethod
    def getResourcesForCollege(cls, queries):
        return queries.filter(Resource.grade == COLLEGE)
    
    @classmethod
    def getResourcesFor6Through8(cls, queries):
        return queries.filter(Resource.grade == GRADE6_8)
    
    @classmethod
    def getResourcesFor9Through12(cls, queries):
        return queries.filter(Resource.grade == GRADE9_12)
    
    @classmethod
    def getResourcesForAlumni(cls, queries):
        return queries.filter(Resource.grade == ALUMNI)
    
    @classmethod
    def getResourcesForSpanish(cls, queries, spanish):
        return queries.filter(Resource.spanish == spanish)
    
    