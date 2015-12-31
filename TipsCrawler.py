'''
@summary: FourSquare Web crawler to find all Venues in Singapore
@author: Philip Wardlaw

Created on Dec 17, 2015
'''

# Python General
import logging
import json
import csv
import sys

# Assets of this Project
from settings import CLIENT_ID, CLIENT_SECRET
from datetime import datetime
from RateLimiter import RateLimiter
from TipRequest import TipRequest
from utils import configureLogging


if __name__ == '__main__':
    startTimeStamp = datetime.now().strftime("%H%M%S")

    configureLogging('TipsCrawler', startTimeStamp)

    log = logging.getLogger('Tips Crawler Root')

    log.info('Starting Tips Crawler')
    log.debug('Initializing Assets')

    if len(sys.argv) != 2 or not sys.argv[1].count('.csv'):
        print 'Please provide the file name of the CSV Venue file.'
        exit(1)

    venuesIds = []
    with open(sys.argv[1], 'r') as fp:
        reader = csv.reader(fp, delimiter='\t')
        for row in reader:
            venuesIds.append(row[0])

    request = TipRequest(CLIENT_ID, CLIENT_SECRET)
    rate = RateLimiter()

    log.info('Beginning retrieval of tips for {0} venues'.format(len(venuesIds)))

    results = {}
    for vId in venuesIds:
        rate.check()
        results[vId] = request.getTipsForVenue(vId)

    log.info('Crawl Complete')
    log.info('{0} tips retrieved.'.format(len(results)))

    filePath = 'output/tips' + startTimeStamp + '.json'
    log.info('Writing file to {0}.'.format(filePath))
    with open(filePath, 'w') as fp:
        json.dump(results, fp)
