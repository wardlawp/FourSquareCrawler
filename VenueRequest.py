'''
@summary: Class for making requests to FourSquare venue search api
@author: Philip Wardlaw
Created on Dec 17, 2015
'''
import requests
import logging
import time

class VenueRequest(object):
    """Class for making requests to FourSquare venue search api
    """
    log = logging.getLogger('VenueRequest')
    MAX_VENUES_PER_REQUEST = 50
    FOURSQUARE_SEARCH_URL = 'https://api.foursquare.com/v2/venues/search'
    API_VERSION = '20140806'
    COUNTRY = 'Singapore'
    TIMEOUT = 30
    INTERNAL_ERROR_RETRY_LIMIT = 5
    
    def __init__(self, clientId, clientSecret):
        self.log.debug('Instantiating VenueRequest')
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.url = self.FOURSQUARE_SEARCH_URL
        self.apiVersion = self.API_VERSION
        self.country = self.COUNTRY
        self.timeout= self.TIMEOUT
        self.__internalErrorRetrys = 0
    
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
        """Get Venues in region denoted by NE SW GPS coordinates
        Keyword arguments:
        NE -- list of two floats, GPS coordinate,s the north east corner of the search rectangle
        SW -- list of two floats, GPS coordinates, the south west corner of the search rectangle
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
                        
        elif response.status_code == 403:
            self.log.warning('Rate limit Exceeded')
            sleepUntil = response.headers.get('X-RateLimit-Reset')
            deltaTime = sleepUntil - time.time()
            self.log.info('Waiting {0} seconds and resuming...'.format(deltaTime))
            time.sleep(deltaTime)
            return self.getVenuesInRegion(NE, SW)
            
        elif (response.status_code == 500) and (self.__internalErrorRetrys < self.INTERNAL_ERROR_RETRY_LIMIT):
            self.log.warning('API Server returns 500, waiting one minute and trying again')
            time.sleep(60)
            self.__internalErrorRetrys += 1
            self.getVenuesInRegion(NE, SW)
            
            
        else:
            self.log.warning('Unhandled HTTP error occurred')
            self.log.warning(response.text)
            self.log.warning(response.url)
            response.raise_for_status()
            