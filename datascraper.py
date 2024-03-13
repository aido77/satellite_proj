#note THIS NOW ONLY CONTAINS THE "REQUESTS" PART OF THE CODE
import pip._vendor.requests #allows to scrape data from websites
import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84

URL = 'http://celestrak.org/NORAD/elements/stations.txt' #this is an "offline" text so i dont get banned again
bigData = load.tle_file(URL) 
#print('Loaded', len(bigData), 'satellites')
    # NORAD contains the latest, up to date TLE data that is non predicted, so items are not constantly changing [updated at 4pm UTC]
#pulls the text from the page and stores it in "bigData"
#print(bigData[2])
