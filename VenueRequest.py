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
    
    def __prepareParams(self, NE, SW):
        payload = {}
        payload['client_id'] = self.clientId
        payload['client_secret'] = self.clientSecret
        # TODO change
        payload['ne'] = "{0},{1}".format(NE[0],NE[1])
        payload['sw'] = "{0},{1}".format(SW[0],SW[1])
        payload['country'] = self.country
        payload['v'] = self.apiVersion
        payload['intent'] = 'browse'
        payload['limit'] = 50
        return payload
    
    def getVenuesInRegion(self, NE, SW):
        """
        
        """
        msg ="Searching for Venues in NE [{0},{1}] SW [{2},{3}]"
        msg =  msg.format(NE[0], NE[1], SW[0], SW[1])
        self.log.info(msg)

        payload = self.__prepareParams(NE, SW)
        response = requests.get(self.url, payload, timeout = self.timeout)
        
        if response.status_code == 200:
            json = response.json()
            
            venues = json['response']['venues']
            self.log.debug('Retreived {0} venues'.format(len(venues)))
            return venues
            #dict: {u'meta': {u'code': 200, u'requestId': u'567549bf498eb63877a59d22'}, u'response': {u'venues': []}}
            
            
                        
        elif response.status_code == 403:
            self.log.warning('Rate limit Exceeded')
            sleepUntil = response.headers.get('X-RateLimit-Reset')
            deltaTime = sleepUntil - time.time()
            self.log.info('Waiting {0} seconds and resuming...'.format(deltaTime))
            time.sleep(deltaTime)
            self.getVenuesInRegion(NE, SW)
            
            
        else:
            self.log.warning('Unhandled http error occurred')
            self.log.warning(response.text)
            self.log.warning(response.url)
            response.raise_for_status()
            
        
        return {}
        #api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=&client_secret=&v=
        

        