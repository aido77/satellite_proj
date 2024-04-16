import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84

global URL
URL = 'http://celestrak.org/NORAD/elements/stations.txt' #this is an "offline" text so i dont get banned again
# NORAD contains the latest, up to date TLE data that is non predicted, so items are not constantly changing [updated at 4pm UTC]
bigData = load.tle_file(URL)
#initialises bigData
