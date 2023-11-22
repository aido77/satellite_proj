import pip._vendor.requests #allows to scrape data from websites
import skyfield
URL = "https://celestrak.org/NORAD/elements/"
# NORAD contains the latest, up to date TLE data that is non predicted, so items are not constantly changing [updated at 4pm UTC]
response = pip._vendor.requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=dmc&FORMAT=tle")
# pulls the "disaster monitoring" satellites data [~10]
# which is a managable dataset
bigData = str(response.text) #pulls the text from the page and stores it in "bigData"
lineCount = 0 #iterative amount of linebreaks [3 needed to split up into seperate full satellite data]
#\r\n indicates linebreak
linesTotal = str(bigData.count("\r\n")) #counts the total amount of line breaks in the string
for i in linesTotal:
    if  bigData.find("\r\n") == True: #if there are any more line breaks
        if lineCount == 3: #if the satellite data is over i.e. three rows have passed
            bigData.split(bigData.find("\r\n")) #NOT SURE [splits it at the next locaton of \r\n???????]
            lineCount = 0 #resets line counter
            i = i+1 #iterates to next cycle
        else:
            bigData[bigData.find("\r\n")] = "" #if satellite data is STILL ONGOING, replace with "" so it doesnt get picked up again
            lineCount = lineCount + 1 #iterates linecount
            i = i + 1 #iterates to next cycle
print(bigData) #prints data

#THIS SHIT DOESNT WORK ^^^^^^^^^^^

#split_bigData = bigData.split("\r\n")
#print(split_bigData)
