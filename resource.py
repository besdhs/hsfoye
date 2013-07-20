'''
Created on Jul 19, 2013

@author: mhotan
'''
from google.appengine.ext import ndb

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
        
    