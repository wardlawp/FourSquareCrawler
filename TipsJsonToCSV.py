'''
Created on Dec 30, 2015

@author: wardlaw
'''
import json as J
import sys
import codecs

if __name__ == '__main__':

    print 'Reading JSON File'

    with codecs.open(sys.argv[1], 'r', encoding='UTF-8') as fp:
        json = J.load(fp)

    print 'Writing output CSV'

    newFile = codecs.open(sys.argv[1].replace('.json', '.csv'), 'w', encoding='UTF-8')

    for key in json:
        tips = json[key]

        line = key + '\t'
        for tip in tips:
            textCleaned = tip['text'].replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
            line += textCleaned + '\t'

        newFile.write(line + '\n')

    newFile.close()

    print 'Finished'
