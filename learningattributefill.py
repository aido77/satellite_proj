import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84
from numpy import sqrt  

learning_sat_mass = {}

learning_sat_mass["ISS (ZARYA)"] = '450000'
learning_sat_mass["ISS (NAUKA)"] = '450000'
learning_sat_mass["CSS (WENTIAN)"] = '100000'
learning_sat_mass["SOYUZ-MS 24"] = '7152'
learning_sat_mass["SHENZHOU-17 (SZ-17)"] = '8100'
learning_sat_mass["PROGRESS-MS 26"] = '2518'
learning_sat_mass["PROGRESS-MS 25"] = '7000'
learning_sat_mass["TIANZHOU-7"] = '14000'
learning_sat_mass["DRAGON CRS-30"] = '2700'



learning_list = list(learning_sat_mass.keys())

#learning_sat_coords = {}
learning_sat_velocity = {}
learning_sat_speed = {}
#learning_sat_g = {}
#learning_sat_force = {}
#learning_sat_radius = {}
learning_database = [[],[]]
total = 0
def learning_attribute_fill():
    tempData = load.tle_file('https://celestrak.org/NORAD/elements/stations.txt')
    count_sat = 0
#A placeholder that shows which satellite we're "on"
    ts = load.timescale()
    t = ts.now()
#gets the current time in epochs
    temp_sat = ''
#a placeholder variable for the satellite data currently being
#   interpreted
    numb_sat = len(tempData)
    while count_sat < numb_sat:
    #this cycles through all of the satellites
        temp_sat = tempData[count_sat]
        #fills temp variable with current satellite data
        for i in range(len(learning_list)):
            #print(learning_list[i])
            if temp_sat.name == learning_list[i]:
                print(temp_sat.name)
                temp_satName = str(temp_sat.name)
                temp_satCoord = temp_sat.at(t).position.km
                #this calculates the coordinates of the satellite at
                #   this particular epoch
                temp_satRadiussqr = (temp_satCoord[0]**2) + (temp_satCoord[1]**2) + (temp_satCoord[2]**2)
                temp_satRadius = (sqrt(temp_satRadiussqr)*1000)
                #adds the satellites name to the dictionary,
                #   along with the coordinates as an array
                temp_satVel = temp_sat.at(t).velocity.m_per_s
                temp_satSpeedsqr = (temp_satVel[0]**2) + (temp_satVel[1]**2) + (temp_satVel[2]**2)
                temp_satSpeed = int(sqrt(temp_satSpeedsqr))
                temp_satAngVel = int(temp_satSpeed) / int(temp_satRadius)
                temp_satForce = (6.6743e-11*5.972e24)/ int(temp_satRadiussqr)
                temp_satMass = int(learning_sat_mass[temp_satName])
                temp_satg = int(temp_satForce)/int(temp_satMass)
                temp_satAcc = int(temp_satSpeedsqr)/int(temp_satRadius)
                temp_satForce = round(temp_satForce,2)
                temp_satSpeed = round(temp_satSpeed,2)
                temp_satMass = round(temp_satMass,2)
                temp_satAngVel = round(temp_satAngVel,6)
                temp_satg = round(temp_satg,2)
                temp_satAcc = round(temp_satAcc,2)
                temp_satRadius = round(temp_satRadius,2)
                learning_database.insert(count_sat,[temp_satName,temp_satAcc,temp_satAngVel,temp_satForce,temp_satg,temp_satMass,temp_satRadius,temp_satSpeed])
                count_sat = count_sat + 1
                next
            else:
                next
        count_sat = count_sat + 1
learning_attribute_fill()
print(learning_database)
