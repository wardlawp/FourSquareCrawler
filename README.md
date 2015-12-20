# FourSquareCrawler
Get all venues in singapore from FourSquare

## Installation
-  Install python 2.7.X (X = 9 or higher)
-  Install project prerequisites: python -m pip install -r requirements.txt
-  Edit settings.py

## Usage
-  Using CMD goto folder
-  Type 'python main.py'
-  Crawling may take several hours
-  Ensure you are on a stable internet connection, preferabbly ethernet over wifi

## Output
-  A log file named 'runtimeHourMinuteSecond.log' in the logs folder. Time corresponds to start time
-  A json file named 'resultsHourMinuteSecond.log' in format { venue_id : venue, venue_id : venue...}
-  See Venue JSON format https://developer.foursquare.com/docs/responses/venue
-  JSON Viewing tool: http://jsonviewer.stack.hu/

## Other
-  To run unit tests: python -m unittest discover tests/

## Ubuntu
The following commands may be necessary on Ubuntu/Linux to install addtional prerequisite

-  sudo apt-get install python-pip python-dev build-essential
-  python -m pip install requests[security]
-  sudo python -m  pip install pyopenssl ndg-httpsclient pyasn1
-  sudo apt-get install libffi-dev libssl-dev

