'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging
import math
import VenueRequest

def isSquare(x):
    root = math.sqrt(x)
    return (root%1.0) == 0

class SearchRectangle(object):
    '''
    classdocs
    '''
    log = logging.getLogger('SearchRectangle')


    def __init__(self, NW, SE, initialDivisions=1, recSubdivisions = 9):
        """
        NW - GPS coordinate, the north west corner of the search rectangle
        SE - GPS coordinate, the south east corner of the search rectangle
        """
        constrMessage ="Instantiating SearchRectangle NW [{0},{1}] SE [{2},{3}]".format(NW[0], NW[1], SE[0], SE[1])
        self.log.debug( constrMessage)
        
        self.NW = NW
        self.SE = SE
        
        assert isSquare(initialDivisions) ,"{0} is not a perfect square".format(initialDivisions) 
        assert isSquare(recSubdivisions), "{0} is not a perfect square".format(recSubdivisions) 
        self.recSubdivisions = recSubdivisions
        self.__subDivisions = [] 
        self.__subDivide(initialDivisions) 
        

    
    def subdivisions(self):
        return self.__subDivisions
    
   
    
    def __subDivide(self, numSubdivisions):
        if(numSubdivisions ==1):
            return
        
        n = int(math.sqrt(numSubdivisions))
        
        dLat = float(self.SE[0] -self.NW[0])/n
        dLong = float(self.SE[1] -self.NW[1])/n
        
        
        
        for divLat in range(n):
            for divLong in range(n):
                NW = [self.NW[0] + dLat*divLat, self.NW[1] + dLong*divLong]
                SW = [NW[0] + dLat, NW[1] + dLong]  
                newSearchRect = SearchRectangle(NW, SW, recSubdivisions = self.recSubdivisions)
                self.__subDivisions.append(newSearchRect)
                
    def search(self, rateLimiter, venueRequest):
        if len(self.__subDivisions) == 0:
            for s in self.__subDivisions:
                s.search(rateLimiter, venueRequest)
        else:
            rateLimiter.check()
            status, results = venueRequest.getVenuesInRegion(self.NW, self.SE)
            if status:
                self.__store(results) #TODO
            else:
                self.log.info("Search failed, creating sub divisions and searching again")
                self.__subDivide(self.recSubdivisions)
                self.search(rateLimiter, venueRequest)
            
        return 'TODO'
        
        
        
        