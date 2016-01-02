'''
@summary: Base Class for making requests to FourSquare api
@author: Philip Wardlaw
Created on Dec 30, 2015
'''

import requests
import logging
import time


class FourSquareRequest(object):
    """ Base Class for making requests to FourSquare api
    """
    API_VERSION = '20140806'
    log = logging.getLogger('FourSquareRequest')

    def __init__(self, clientId, clientSecret, url):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.url = url
        self.apiVersion = self.API_VERSION

    def makeRequest(self, url, payload, responseHandler, retryMethod):
        try:
            response = requests.get(url, payload)

            if response.status_code == 200:
                return responseHandler(response)

            elif response.status_code == 403:
                self.log.warning('Rate limit Exceeded')
                sleepUntil = int(response.headers.get('x-rateLimit-reset'))
                deltaTime = sleepUntil - time.time() + 300
                self.log.warning('Waiting {0} seconds and'.format(deltaTime) +
                                 ' resuming...')

                time.sleep(int(deltaTime))
                return retryMethod()

            elif (response.status_code == 500) and (self.__internalErrorRetrys < self.INTERNAL_ERROR_RETRY_LIMIT):

                self.log.warning('API Server returns 500, waiting one' +
                                 ' minute and trying again')
                time.sleep(60)
                self.__internalErrorRetrys += 1
                return retryMethod()

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
                return retryMethod()
            else:
                self.log.warning('Maximum retries performed,'
                                 ' throwing exception...')
                raise e



