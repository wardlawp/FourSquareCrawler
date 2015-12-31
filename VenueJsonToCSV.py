'''
Created on Dec 30, 2015

@author: wardlaw
'''
import json as J
import sys
import codecs

if __name__ == '__main__':

    if len(sys.argv) != 2 or not sys.argv[1].count('.json'):
        print 'Please provide the file name of the JSON Venue file.'
        exit(1)

    print 'Reading JSON File'
    with codecs.open(sys.argv[1], 'r', encoding='UTF-8') as fp:
        json = J.load(fp)

    print 'Writing output CSV'
    newFile = codecs.open(sys.argv[1].replace('.json', '.csv'), 'w', encoding='UTF-8')
    for key in json:
        venue = json[key]
        line = key + '\t' \
            + venue['name'] + '\t' \
            + str(venue['location']['lat']) + '\t' \
            + str(venue['location']['lng']) + '\t'

        for c in venue['categories']:
            line += c['name'] + '\t'

        newFile.write(line + '\n')

    newFile.close()

    print 'Finished'
