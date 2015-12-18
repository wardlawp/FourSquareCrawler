'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging

class ResultsContainer(object):
    '''
    A static contained of unique Results
    '''
    
    log = logging.getLogger('ResultsContainer')
    
    def __init__(self):
        self.log.info('Instantiating ResultsContainer')
        self.storage = []

    def store(self, results):
        #Todo check uniqueness
        self.storage.append(results)
        

    def writeToFile(self,filepath):
        #todo: implement
        pass