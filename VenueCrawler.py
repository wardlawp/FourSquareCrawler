'''
@summary: FourSquare Web crawler to find all Venues in Singapore
@author: Philip Wardlaw

Created on Dec 17, 2015
'''

# Python General
import logging
import json


# Assets of this Project
from settings import *
from SearchRectangle import SearchRectangle
from datetime import datetime
from RateLimiter import RateLimiter
from VenueRequest import VenueRequest
from utils import configureLogging

if __name__ == '__main__':
    startTimeStamp = datetime.now().strftime("%H%M%S")

    configureLogging('VenueCrawler', startTimeStamp)

    log = logging.getLogger('Venue Crawler Root')

    log.info('Starting Venue Crawler')

    log.debug('Initializing Assets')
    searchRect = SearchRectangle(SEARCH_NE, SEARCH_SW, 100, 25)
    request = VenueRequest(CLIENT_ID, CLIENT_SECRET)
    rate = RateLimiter()

    log.info('Beginning Search on NE {0} SW {1}'.format(SEARCH_NE, SEARCH_SW))
    results = searchRect.search(rate, request)

    log.info('Crawl Complete')
    log.info('{0} venues captured.'.format(len(results)))

    filePath = 'output/venues' + startTimeStamp + '.json'
    log.info('Writing file to {0}.'.format(filePath))
    with open(filePath, 'w') as fp:
        json.dump(results, fp)
