import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84
from numpy import sqrt  

learning_sat_mass = {}

learning_sat_mass["ISS (ZARYA)"] = '450000'
learning_sat_mass["CSS (WENTIAN)"] = '100000'
learning_sat_mass["SOYUZ-MS 24"] = '7152'
learning_sat_mass["SHENZHOU-17 (SZ-17)"] = '8100'
learning_sat_mass["PROGRESS-MS 26"] = '2518'    
learning_sat_mass["PROGRESS-MS 25"] = '7000'
learning_sat_mass["TIANZHOU-7"] = '14000'
learning_sat_mass["DRAGON CRS-30"] = '2700'
learning_sat_mass["SL-4 R/B"] = '2355'
learning_sat_mass["DRAGON CRS-30"] = '2841'
#creates and fills dictinary with satellites and their corresponding masses
learning_list = list(learning_sat_mass.keys())
#creates a list that contains the names of these satellites

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
            if temp_sat.name == learning_list[i]:
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
                temp_satSpeed = float(sqrt(temp_satSpeedsqr))
                #uses pythagoras' theorem to get linear speed
                temp_satMass = float(learning_sat_mass[temp_satName]) #references the dictionary by name to get  mass
                temp_satg = (3.98e14)/ (float(temp_satRadiussqr)*1000000)
                temp_satForce = float(temp_satg)*float(temp_satMass)
                temp_satAngVel = sqrt(float(temp_satForce) / (float(temp_satMass)*float(temp_satRadius)))
                temp_satAcc = float(temp_satSpeedsqr)/float(temp_satRadius)
                #initialises and calculates variables using the formula in the A Level Physics OCR A data formulae booklet
                temp_satForce = round(temp_satForce,2)
                temp_satSpeed = round(temp_satSpeed,0)
                temp_satMass = round(temp_satMass,0)
                temp_satAngVel = round(temp_satAngVel,5)
                temp_satg = round(temp_satg,2)
                temp_satAcc = round(temp_satAcc,2)
                temp_satRadius = round(temp_satRadius,0)
                #rounds these values to be suitable and accurate
                learning_database.insert(count_sat,[temp_satName,temp_satAcc,temp_satAngVel,temp_satForce,temp_satg,temp_satMass,temp_satRadius,temp_satSpeed])
                #adds these variables to the database
                count_sat = count_sat + 1
                next
            else:
                next
        count_sat = count_sat + 1
    learning_database.pop(1)
    learning_database.pop(1)
#gets rid of the two [][] used to define the 2D array
