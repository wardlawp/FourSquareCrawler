'''
@summary: FourSquare Web crawler to find all tips for given list of venues
@author: Philip Wardlaw

Created on Dec 29, 2015
'''

# Python General
import logging
import json
import csv
import sys
from datetime import datetime

# Assets of this Project
from settings import CLIENT_ID, CLIENT_SECRET
from Utils import configureLogging
from Requests import TipRequest
from VenueTipRepo import VenueTipRepo


if __name__ == '__main__':
    startTimeStamp = datetime.now().strftime("%H%M%S")

    configureLogging('TipsCrawler', startTimeStamp)

    log = logging.getLogger('Tips Crawler Root')

    log.info('Starting Tips Crawler')
    log.debug('Initializing Assets')

    if len(sys.argv) != 2 or not sys.argv[1].count('.csv'):
        log.warn('Please provide the file name of the CSV Venue file.')
        log.warn('Exiting')
        exit(1)

    log.info('Reading venue CSV input')
    venuesIds = []
    with open(sys.argv[1], 'r') as fp:
        reader = csv.reader(fp, delimiter='\t')
        for row in reader:
            if len(row) != 0:
                venuesIds.append(row[0])

    request = TipRequest(CLIENT_ID, CLIENT_SECRET)

    log.info('Beginning retrieval of tips for {0} venues'
             .format(len(venuesIds)))

    repo = VenueTipRepo()
    totalLen = len(venuesIds)
    curr = 0
    for vId in venuesIds:
        log.info('{0}/{1} Venues'.format(curr, totalLen))

        if(repo.hasTips(vId)):
            log.info('Tips Venue {0} already retrieved'.format(vId))
        else:
            log.info('Retrieving Tips for Venue {0}'.format(vId))
            repo.addVenueTips(vId, request.getTipsForVenue(vId))

        curr += 1

    log.info('Crawl Complete')
    log.info('{0} tip sets retrieved.'.format(repo.count()))

    filePath = 'output/tips' + startTimeStamp + '.json'
    log.info('Writing file to {0}.'.format(filePath))
    with open(filePath, 'w') as fp:
        tips = repo.all()
        json.dump(tips, fp)
