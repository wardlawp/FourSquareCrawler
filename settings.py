'''
@summary: Settings for project
@author: Philip Wardlaw
Created on Dec 17, 2015
'''

# FourSquare Application ID and secret
#    Create yourself a FourSquare developer profile
#    https://foursquare.com/login?continue=%2Fdevelopers%2Fapps
#    add an app (you can make up the details) and copy the key and secret here
CLIENT_ID = '0NMBABZPYKO31STLF5PE3GWRL32DNMKZUIKHHVOF5FE4FDHR'
CLIENT_SECRET = 'T2QYMUAVN1HJQXCQVRHQTFUFPONSPZBMWB3JJ2JFV5TR3OGT'

# GPS Coordinates bounding Singapore
# Obtained from Google Maps
# See http://www.darrinward.com/lat-long/?id=1671068
# Note only Singapore venues will be stored (Malaysia will be ignored)
SEARCH_NE = [1.471, 104.086133]
SEARCH_SW = [1.136524, 103.606576]
