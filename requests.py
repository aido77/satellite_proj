import pip._vendor.requests #allows to scrape data from websites
import skyfield
URL = "https://celestrak.org/NORAD/elements/"
# NORAD contains the latest, up to date TLE data that is non predicted, so items are not constantly changing [updated at 4pm UTC]
response = pip._vendor.requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=dmc&FORMAT=tle")
# pulls the "disaster monitoring" satellites data [~10]
# which is a managable dataset
bigData = str(response.text)
print(bigData)
