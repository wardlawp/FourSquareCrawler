'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import time, logging

class RateLimiter(object):
    '''
    classdocs
    '''
    FourSpaceLimit = 5000
    HOUR = 3600
    log = logging.getLogger('RateLimiter')

    def __init__(self):
        '''
        Constructor
        '''
        self.log.debug('Instantiating RateLimiter')
        self.times = []
       
    def check(self):
        self.times.append(time.time())
        self.__filterTimes()
        
        eventsInLastHour = len(self.times)
        
        if eventsInLastHour > RateLimiter.FourSpaceLimit:
            self.log.warn('ABOUT TO EXCEED RATE LIMIT! Sleeping 1 minute to avoid exceeding rate')
            time.sleep(60)

    def __filterTimes(self):
        timeNow = time.time()       
        for t in self.times:
            if timeNow - t > RateLimiter.HOUR:
                self.times.remove(t)

        
        
