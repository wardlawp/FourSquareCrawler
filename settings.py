'''
@summary: Settings for project
@author: Philip Wardlaw
Created on Dec 17, 2015
'''

# FourSquare Application ID and secret
#    Create yourself a FourSquare developer profile
#    https://foursquare.com/login?continue=%2Fdevelopers%2Fapps
#    add an app (you can make up the details) and copy the key and secret here
CLIENT_ID = ''
CLIENT_SECRET = ''

# GPS Coordinates bounding Singapore
# Obtained from Google Maps
# See http://www.darrinward.com/lat-long/?id=1671068
# Note only Singapore venues will be stored (Malaysia will be ignored)
SEARCH_NE = [1.471, 104.086133]
SEARCH_SW = [1.136524, 103.606576]
