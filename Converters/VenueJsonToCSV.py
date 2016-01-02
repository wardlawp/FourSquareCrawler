'''
@summary: Converts output of VenueCrawler.py to CSV
@author: Philip Wardlaw
Created on Dec 30, 2015

STAND ALONE SCRIPT
'''
import json as J
import sys
import codecs

delim = '\t'


def stripChars(aString):
    return aString.replace('\t', ' ') \
                  .replace('\n', ' ') \
                  .replace('\r', ' ')

if __name__ == '__main__':

    if len(sys.argv) != 2 or not sys.argv[1].count('.json'):
        print 'Please provide the file name of the JSON Venue file.'
        exit(1)

    print 'Reading JSON File'
    with codecs.open(sys.argv[1], 'r', encoding='UTF-8') as fp:
        json = J.load(fp)

    print 'Writing output CSV'
    newFile = codecs.open(sys.argv[1].replace('.json', '.csv'),
                          'w', encoding='UTF-8')
    for key in json:
        venue = json[key]

        line = key + delim \
            + stripChars(venue['name']) \
            + delim \
            + str(venue['location']['lat']) \
            + delim \
            + str(venue['location']['lng']) \
            + delim

        for c in venue['categories']:
            line += stripChars(c['name']) + delim

        newFile.write(line + '\n')

    newFile.close()

    print 'Finished'
