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

startTimeStamp = datetime.now().strftime("%H%M%S")


def configureLogging():
    """ Configure logging to write debug, info, warning messages to file,
    and write info and warning messages to console.

    Code copied from Python docs.
    """
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s' +
                               ' %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='logs/runtime' + startTimeStamp + '.log',
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    configureLogging()

    log = logging.getLogger('AppRoot')

    log.info('Starting Crawler')

    log.debug('Initializing Assets')
    searchRect = SearchRectangle(SEARCH_NE, SEARCH_SW, 100, 25)
    request = VenueRequest(CLIENT_ID, CLIENT_SECRET)
    rate = RateLimiter()

    log.info('Beginning Search on NE {0} SW {1}'.format(SEARCH_NE, SEARCH_SW))
    results = searchRect.search(rate, request)

    log.info('Crawl Complete')
    log.info('{0} venues captured.'.format(len(results)))

    filePath = 'output/results' + startTimeStamp + '.json'
    log.info('Writing file to {0}.'.format(filePath))
    with open(filePath, 'w') as fp:
        json.dump(results, fp)
