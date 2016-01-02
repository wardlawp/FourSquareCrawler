# FourSquareCrawlers and Converters

-  Get all venues in singapore from FourSquare
-  Get all tips for a list of venues
-  Convert json output from crawlers to easy to read csv format

## Installation

-  Install python 2.7.X (X = 9 or higher)
-  Install project prerequisites: python -m pip install -r requirements.txt
-  Edit settings.py

## Usage

-  Crawling may take several hours
-  Ensure you are on a stable internet connection, preferabbly ethernet over wifi
-  Typical usage: VenueCrawler > VenueJsonToCSV > TipsCrawler > TipsJsonToCSV

### VenueCrawler

-  Navigate to root folder
-  Run using command 'python VenueCrawler.py' 
-  A json file named 'venuesTIMESTAMP.json' will be produced
-  JSON file format: { venue_id : venue, venue_id : venue...}
-  See Venue JSON format https://developer.foursquare.com/docs/responses/venue

### VenueJsonToCSV

-  Navigate to root folder
-  Run using command 'python Converters/VenueJsonToCSV.py output/V.json'
-  Where V.json is the output from the VenueCrawler
-  A V.csv file will be created in the output folder 

### TipsCrawler 

-  Requires output from VenueCrawler in csv to run, see previous sections
-  Navigate to root folder
-  Run using command 'python TipsCrawler.py output/V.csv' 
-  A json file named 'tipsTIMESTAMP.json' will be produced
-  JSON file format: { venue_id : [tips_count, [tips]]}
-  See Tip JSON format https://developer.foursquare.com/docs/responses/tip

### TipsJsonToCSV

-  Navigate to root folder
-  Run using command 'python Converters/VenueJsonToCSV.py output/T.json'
-  Where T.json is the output from the TipsCrawler
-  A T.csv file will be created in the output folder 

## Other

-  If an error occurs please see the log file for the Crawler you where using in logs/
-  The JSON files will be huge, you can try opening them using chrome
-  JSON Viewing tool: http://jsonviewer.stack.hu/ (may not work for huge files)

## Ubuntu

The following commands may be necessary on Ubuntu/Linux to install addtional prerequisite

-  sudo apt-get install python-pip python-dev build-essential
-  python -m pip install requests[security]
-  sudo python -m  pip install pyopenssl ndg-httpsclient pyasn1
-  sudo apt-get install libffi-dev libssl-dev

