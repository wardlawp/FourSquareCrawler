'''
@summary: Keep track of request rate and limit process if necessary
@author: Philip Wardlaw
Created on Dec 17, 2015
'''
import time, logging

class RateLimiter(object):
    """Keeps track of number of actions per hour, sleeps thread if number of
    actions exceeds a limit.
    """
    FourSquareLimit = 5000
    HOUR = 3600
    log = logging.getLogger('RateLimiter')

    def __init__(self):
        self.log.debug('Instantiating RateLimiter')
        self.times = []
       
    def check(self):
        """ Check that limit isn't going to be exceeded, sleep if it is.
        This method should be called everything before a request to the 
        FourSquare api is made.
        """
        self.times.append(time.time())
        self.__filterTimes()
        
        eventsInLastHour = len(self.times)
        
        if eventsInLastHour > RateLimiter.FourSquareLimit:
            self.log.warn('ABOUT TO EXCEED RATE LIMIT! Sleeping 1 minute to avoid exceeding rate')
            time.sleep(60)

    def __filterTimes(self):
        timeNow = time.time()       
        for t in self.times:
            if timeNow - t > RateLimiter.HOUR:
                self.times.remove(t)

        
        
