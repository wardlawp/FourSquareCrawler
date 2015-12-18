'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging
from SearchRectangle import SearchRectangle
from datetime import datetime
from Results import Results

def configureLogging():
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='myapp' + datetime.now().strftime("%H%M%S") +'.log',
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
    
    searchRect = SearchRectangle([1.459812, 103.575513], [1.187969, 104.127510], 100, 16)
    searchRect.search()
    Results.writeToFile("output.json")
        

    
