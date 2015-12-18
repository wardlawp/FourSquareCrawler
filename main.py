'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging
from SearchRectangle import SearchRectangle
from datetime import datetime
from RateLimiter import RateLimiter
from VenueRequest import VenueRequest

def configureLogging():
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='runtime' + datetime.now().strftime("%H%M%S") +'.log',
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


CLIENT_ID = '0NMBABZPYKO31STLF5PE3GWRL32DNMKZUIKHHVOF5FE4FDHR'
CLIENT_SECRET = 'T2QYMUAVN1HJQXCQVRHQTFUFPONSPZBMWB3JJ2JFV5TR3OGT'
SINGAPORE_NW = [1.459812, 103.575513]
SINGAPORE_SE = [1.187969, 104.127510]

if __name__ == '__main__':
    configureLogging()
    
    log = logging.getLogger('AppRoot')
    log.info('Starting Crawler')
    
    log.debug('Initializing Assets')
    searchRect = SearchRectangle(SINGAPORE_NW, SINGAPORE_SE , 100, 16)
    request = VenueRequest(CLIENT_ID, CLIENT_SECRET)
    rate = RateLimiter()
    
    log.debug('Beginning Search')
    json = searchRect.search(rate, request)
    
        

    
