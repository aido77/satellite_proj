from datascraper import *

numb_Sat = len(bigData)
count_sat = 0
coords = {}
ts = load.timescale()
t = ts.now()
temp_sat = ''

while count_sat < numb_Sat:
    temp_sat = bigData[count_sat]
    temp_satCoord = temp_sat.at(t).position.km
    coords[temp_sat.name] = temp_satCoord
    count_sat = count_sat + 1


print(coords)
