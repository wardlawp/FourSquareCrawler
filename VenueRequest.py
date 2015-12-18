'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import requests
import logging
import time

class VenueRequest(object):
    '''
    classdocs
    '''
    log = logging.getLogger('VenueRequest')
    MAX_VENUES_PER_REQUEST = 50
    FOURSQUARE_SEARCH_URL = 'https://api.foursquare.com/v2/venues/search'
    API_VERSION = '20140806'
    COUNTRY = 'Singapore'
    TIMEOUT = 30
    
    
    def __init__(self, clientId, clientSecret):
        self.log.debug('Instantiating VenueRequest')
        
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.url = self.FOURSQUARE_SEARCH_URL
        self.apiVersion = self.API_VERSION
        self.country = self.COUNTRY
        self.timeout= self.TIMEOUT
    
    
    
    def getVenuesInRegion(self,NW, SE):
        """
        
        """
        msg ="Searching for Venues in NW [{0},{1}] SE [{2},{3}]"
        msg =  msg.format(NW[0], NW[1], SE[0], SE[1])
        self.log.info(msg)

        payload = {'NW': NW, 'SE': SE, 'country': self.country, 'v' : self.apiVersion }
        # TODO
        # limit :50
        # ll : 32.4,-56.5 //dont think this is needed
        # intent: browse
        # ne sw! TODO
        # client_id
        # client_secret
        
        response = requests.get(self.url, payload, timeout = self.timeout)
        
        if response.status_code == 200:
            json = response.json()
            
            #TODO determine json length
            if json.length >= self.MAX_VENUES_PER_REQUEST:
                return False, []
            else:
                return True, json
            
        elif response.status_code == 403:
            self.log.warning('Rate limit Exceeded')
            sleepUntil = response.headers.get('X-RateLimit-Reset')
            #TODO actually work out deltaTime
            deltaTime = sleepUntil - time.time()
            self.log.info('Waiting {0} seconds and resuming...'.format(deltaTime))
            time.sleep(deltaTime)
            self.getVenuesInRegion(NW, SE)
        
        else:
            self.log.warning('Unhandled http error occured')
            response.raise_for_status()
            
        
        return False, []
        #api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=&client_secret=&v=
        

        