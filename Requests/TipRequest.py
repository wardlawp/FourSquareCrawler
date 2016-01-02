'''
@summary: Class for making requests to FourSquare Tip api
@author: Philip Wardlaw
Created on Dec 30, 2015
'''

import logging
import json
from FourSquareRequest import FourSquareRequest


class TipRequest(FourSquareRequest):
    """Class for making requests to FourSquare Tip API
    """
    log = logging.getLogger('TipRequest')
    MAX_TIPS_PER_REQUEST = 500
    FOURSQUARE_TIPS_URL = 'https://api.foursquare.com/v2/venues/{0}/tips'
    INTERNAL_ERROR_RETRY_LIMIT = 5

    def __init__(self, clientId, clientSecret):
        self.log.debug('Instantiating TipRequest')
        super(FourSquareRequest, self).__init__(clientId,
                                                clientSecret,
                                                self.FOURSQUARE_TIPS_URL)



    def __prepareParams(self, offset):
        payload = {}
        payload['client_id'] = self.clientId
        payload['client_secret'] = self.clientSecret
        payload['v'] = self.apiVersion
        payload['limit'] = self.MAX_TIPS_PER_REQUEST
        payload['offset'] = offset
        return payload

    def __handleResonse(self, response):
        json = response.json()

        items = json['response']['tips']['items']
        count = len(items)

        if count == self.MAX_TIPS_PER_REQUEST:
            m = self.MAX_TIPS_PER_REQUEST
            newOffset = offset + m

            msg = 'Number of Tips exceeds limit,' \
                  ' recursing with offset {0}'

            self.log.info(msg.format(newOffset))

            rCount, rItems = self.getTipsForVenue(venueId, newOffset)
            count += rCount
            items += rItems

        return count, items


    def getTipsForVenue(self, venueId, offset=0):
        """Get Tips for a Venue
        """

        msg = "Requesting Tips for Venue {0}".format(venueId)
        self.log.info(msg)

        self.makeRequest(self.url.format(venueId),
                         self.__prepareParams(offset),
                         self.__handleResonse,
                         )
        payload = 
        url = 

        try:
            response = requests.get(url, payload)

            if response.status_code == 200:
                

            elif response.status_code == 404:
                # Venue no loner exists
                return 0, []

            elif response.status_code == 403:
                self.log.warning('Rate limit Exceeded')
                sleepUntil = int(response.headers.get('x-rateLimit-reset'))
                deltaTime = sleepUntil - time.time() + 300
                self.log.warning('Waiting {0} seconds and'.format(deltaTime) +
                                 ' resuming...')

                time.sleep(int(deltaTime))
                return self.getTipsForVenue(venueId, offset)

            elif (response.status_code == 500) and (self.__internalErrorRetrys < self.INTERNAL_ERROR_RETRY_LIMIT):

                self.log.warning('API Server returns 500, waiting one' +
                                 ' minute and trying again')
                time.sleep(60)
                self.__internalErrorRetrys += 1
                return self.getTipsForVenue(venueId, offset)

            else:
                self.log.warning('Unhandled HTTP error occurred')
                self.log.warning(response.text)
                response.raise_for_status()

        except Exception as e:
            self.log.warning('Unhandled Exception occurred')

            if (self.__internalErrorRetrys < self.INTERNAL_ERROR_RETRY_LIMIT):
                self.log.warning('Waiting one minute and trying again')
                time.sleep(60)
                self.__internalErrorRetrys += 1
                return self.getTipsForVenue(venueId, offset)
            else:
                self.log.warning('Maximum retries performed,' +
                                 ' throwing exception...')
                raise e
