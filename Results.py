'''
Created on Dec 17, 2015

@author: Philip Wardlaw
'''
import logging

class Results(object):
    '''
    A static contained of unique Results
    '''
    storage = []
    log = logging.getLogger('Results')
        
    @staticmethod
    def store(results):
        #Todo check uniqueness
        Results.storage.append(results)
        
    @staticmethod
    def writeToFile(filepath):
        #todo: implement
        pass