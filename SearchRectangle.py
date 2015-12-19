'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging
import math
from VenueRequest import VenueRequest

def isSquare(x):
    root = math.sqrt(x)
    return (root%1.0) == 0

class SearchRectangle(object):
    '''
    classdocs
    '''
    log = logging.getLogger('SearchRectangle')


    def __init__(self, NE, SW, initialDivisions=1, recSubdivisions = 9):
        """
        NE - GPS coordinate, the north west corner of the search rectangle
        SW - GPS coordinate, the south east corner of the search rectangle
        """
        constrMessage ="Instantiating SearchRectangle NE [{0},{1}] SW [{2},{3}]".format(NE[0], NE[1], SW[0], SW[1])
        self.log.debug( constrMessage)
        
        self.NE = NE
        self.SW = SW
        
        assert isSquare(initialDivisions) ,"{0} is not a perfect square".format(initialDivisions) 
        assert isSquare(recSubdivisions), "{0} is not a perfect square".format(recSubdivisions) 
        self.recSubdivisions = recSubdivisions
        self.__subDivisions = [] 
        self.__subDivide(initialDivisions) 
        
        self.__results = {}
        

    
    def subdivisions(self):
        return self.__subDivisions
    
   
    
    def __subDivide(self, numSubdivisions):
        if(numSubdivisions ==1):
            return
        
        n = int(math.sqrt(numSubdivisions))
        
        dLat = float(self.SW[0] -self.NE[0])/n
        dLong = float(self.SW[1] -self.NE[1])/n
        
        for divLat in range(n):
            for divLong in range(n):
                NW = [self.NE[0] + dLat*divLat, self.NE[1] + dLong*divLong]
                SW = [NW[0] + dLat, NW[1] + dLong]  
                newSearchRect = SearchRectangle(NW, SW, recSubdivisions = self.recSubdivisions)
                self.__subDivisions.append(newSearchRect)
                
                
    def search(self, rateLimiter, venueRequest):
        if len(self.__subDivisions) != 0:
            for s in self.__subDivisions:
                self.__addResults(s.search(rateLimiter, venueRequest))
        else:
            rateLimiter.check()
            results = venueRequest.getVenuesInRegion(self.NE, self.SW)
            
            if len(results) < VenueRequest.MAX_VENUES_PER_REQUEST: 
                self.__store(results) #TODO
            else:
                self.log.warn("MAX_VENUES_PER_REQUEST exceeded. Sub dividing region to find additional venues")
                self.__subDivide(self.recSubdivisions)
                self.__addResults(self.search(rateLimiter, venueRequest))
            
        return self.__results
    
    def __store(self, newResults):
        
        for r in newResults:
            self.__results[r['id']] = r
        
    def __addResults(self, newResults):
        
        for key, val in newResults.items():
            self.__results[key] = val
        
        