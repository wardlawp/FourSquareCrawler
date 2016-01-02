'''
@summary: Persistence Class for storing serialized tips

This file can be executed to clear the database, or print it's contents

@author: Philip Wardlaw
Created on Jan 1, 2016
'''

import sys
import logging
import sqlite3 as lite
import json


class VenueTipRepo(object):
    """Persistence Class for storing serialized tips
    """
    log = logging.getLogger('VenueTipRepo')
    STANDARD_FILE_PATH = 'VenueTips.db'

    def __init__(self, filePath=STANDARD_FILE_PATH):
        self.log.debug('Instantiating VenueTipRepo')
        self.fp = filePath
        self.con = lite.connect(self.fp)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS'
                         ' VenueTips(venueId TEXT UNIQUE, tips TEXT);')

    def addVenueTips(self, venueId, tips):
        """Add tips for a given venue to the repo
        Keyword arguments:
        venueId -- string venue id
        tips -- array object of tips
        """
        assert isinstance(venueId, str)

        self.log.info('Adding tips for Venue {0} to VenueTipRepo {1}'
                      .format(venueId, self.fp))

        qryData = (venueId, json.dumps(tips))
        self.cur.execute("INSERT INTO VenueTips VALUES(? , ?);", qryData)
        self.con.commit()

    def removeTip(self, venueId):
        assert isinstance(venueId, str)
        self.log.info('Deleting tips for Venue {0} from VenueTipRepo {1}'
                      .format(venueId, self.fp))
        self.cur.execute("DELETE FROM VenueTips Where venueId = ?;", (venueId,))
        self.con.commit()

    def hasTips(self, venueId):
        """Test if tips for venueId are in repo
        returns boolean
        """
        assert isinstance(venueId, str)
        self.cur.execute("SELECT COUNT(*) FROM VenueTips Where venueId = ?;",
                         (venueId,))
        result = self.cur.fetchone()

        return int(result[0]) > 0

    def getTip(self, venueId):
        """
        returns array
        """
        assert isinstance(venueId, str)
        self.cur.execute("SELECT * FROM VenueTips Where venueId = ?;",
                         (venueId,))
        return json.loads(self.cur.fetchone())

    def clearAll(self):
        self.log.info('Deleting all tips from VenueTipRepo {0}'
                      .format(self.fp))
        self.cur.execute("DELETE FROM VenueTips;")
        self.con.commit()

    def all(self):
        """ Get dict of all tips
        returns dict {string venueId : array tips }
        """
        self.cur.execute("SELECT * FROM VenueTips;")
        results = self.cur.fetchall()
        resultDict = {}

        for r in results:
            resultDict[r[0]] = json.loads(r[1])

        return resultDict

    def count(self):
        "Count the total number of venues that tips are stored for"
        self.cur.execute("SELECT COUNT(*) FROM VenueTips;")
        result = self.cur.fetchone()
        return int(result[0])

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    repo = VenueTipRepo()
    if len(sys.argv) == 2 and sys.argv[1] == 'clear':
        question = 'Are you sure you want to clear {0}? [y,n]' \
                    .format(repo.fp)

        if raw_input(question).lower() == 'y':
            print 'Clearing all tips'
            repo.clearAll()
            print 'Done'

    elif len(sys.argv) == 2 and sys.argv[1] == 'print':
        print repo.all()
