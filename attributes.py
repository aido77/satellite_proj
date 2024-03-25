from datascraper import *
import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84
from numpy import sqrt
#imports all of the already imported libraries and variables
coords = {}
velocity = {}
speed = {}
attribute_list = [[],[]]
#a dictionary where the coordinates of the satellites, along with
#   the names, are placed
def attribute_refresh(numb_Sat, URL2):
    tempData = load.tle_file(URL2, reload=True)
    #this shows the number of satellites in bigData
    count_sat = 0
    list_sat = count_sat + 1
#A placeholder that shows which satellite we're "on"
    ts = load.timescale()
    t = ts.now()
#gets the current time in epochs
    temp_sat = ''
#a placeholder variable for the satellite data currently being
#   interpreted
    if len(coords) > len(tempData):
        coords.clear()
        attribute_refresh(numb_Sat, URL)
    else:
        while count_sat < numb_Sat:
#this cycles through all of the satellites
            temp_sat = tempData[count_sat]
            temp_satName = temp_sat.name
            print(temp_sat)
    #fills temp variable with current satellite data
            temp_satCoord = temp_sat.at(t).position.km
            temp_satTime = temp_sat.epoch.utc_strftime()
    #this calculates the coordinates of the satellite at
    #   this particular epoch
            coords[temp_sat.name,temp_sat.epoch] = temp_satCoord
    #adds the satellites name to the dictionary,
    #   along with the coordinates as an array
            temp_satVel = temp_sat.at(t).velocity.m_per_s
            velocity[temp_sat.name,temp_sat.epoch] = temp_satVel
            x = int(temp_satVel[0])
            y = int(temp_satVel[1])
            z = int(temp_satVel[2])
            temp_satSpeedsqr = (x**2) + (y**2) + (z**2)
            temp_satSpeed = sqrt(temp_satSpeedsqr)
            attribute_list.insert(list_sat,[temp_satName,temp_satTime,temp_satCoord,temp_satVel,temp_satSpeed])
            speed[temp_sat.name,temp_sat.epoch] = temp_satSpeed
            count_sat = count_sat + 1
            list_sat = list_sat + 1
            print(len(attribute_list))
    #iterates to the next satellite
    return
def attribute_clear():
    coords = {}
    velocity = {}
    speed = {}
