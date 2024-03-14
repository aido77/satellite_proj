from datascraper import *
#imports all of the already imported libraries and variables
numb_Sat = len(bigData) 
#this shows the number of satellites in bigData
count_sat = 0
#A placeholder that shows which satellite we're "on"
coords = {}
#a dictionary where the coordinates of the satellites, along with
#   the names, are placed
ts = load.timescale()
t = ts.now()
#gets the current time in epochs
temp_sat = ''
#a placeholder variable for the satellite data currently being
#   interpreted
while count_sat < numb_Sat:
#this cycles through all of the satellites
    temp_sat = bigData[count_sat]
    #fills temp variable with current satellite data
    temp_satCoord = temp_sat.at(t).position.km
    #this calculates the coordinates of the satellite at
    #   this particular epoch
    coords[temp_sat.name] = temp_satCoord
    #adds the satellites name to the dictionary,
    #   along with the coordinates as an array
    count_sat = count_sat + 1
    #iterates to the next satellite

print(coords)
