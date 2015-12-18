'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
from SearchRectangle import SearchRectangle
import requests
import logging

class Venue(object):
    '''
    classdocs
    '''
    log = logging.getLogger('Venue')


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def getVenuesFromFourSquare(searchRect):
        assert isinstance(searchRect, SearchRectangle)
        Venue.log.info("Inside static method")
        
        #api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=0NMBABZPYKO31STLF5PE3GWRL32DNMKZUIKHHVOF5FE4FDHR&client_secret=T2QYMUAVN1HJQXCQVRHQTFUFPONSPZBMWB3JJ2JFV5TR3OGT&v=20140806
        
    def test(self):
        return 'test'
        