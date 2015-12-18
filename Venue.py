'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
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
    def getVenuesFromFourSquare(NW, SE):
        Venue.log.info("Searching for Venues in NW [{0},{1}] SE [{2},{3}]".format(NW[0], NW[1], SE[0], SE[1]))
        Venue.log.warning("Search Not Implemented")
        return False, []
        #api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=0NMBABZPYKO31STLF5PE3GWRL32DNMKZUIKHHVOF5FE4FDHR&client_secret=T2QYMUAVN1HJQXCQVRHQTFUFPONSPZBMWB3JJ2JFV5TR3OGT&v=20140806
        

        