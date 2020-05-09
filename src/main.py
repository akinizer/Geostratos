import googlemaps, requests as rq, json, pandas as pd, numpy as np, geocoder, os, geopy, gmplot.gmplot as gp, math, random, webbrowser
from geopy.distance import great_circle

from datetime import datetime

api_key = "AIzaSyCoyLKNRnhMJZCMz7DCkwUnlipIRU88_zU";
os.environ["GOOGLE_API_KEY"] = api_key
markerArr = ["yellow", "blue", "green", "red", "cornflowerblue", "orange", "gray"]

# url of the text search dictionary
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# give keywords like "places/hotels/best beach in Ankara/Delhi/
def findLocationWith(keywords):

    # keywords to filter results to gather from query search
    query = keywords

    # get a query of google map search using a dictionary url and application secret key for authorization
    r = rq.get(url + 'query=' + query + '&key=' + api_key)

    # get information of data from a list of results as array of strings
    y = r.json()['results']

    # print("Format: ", y[0],"\n") -> The list of query columns: formatted_address, geometry(lat,lng),
    # viewport(northeast(lat,lng)), northwest(lat,lng), icon, id, name,
    # photos(height,html_attributions,photo_reference,width), place_id, reference, types, political

    # keep looping upto length of y
    for i in range(len(y)):

        # Print name and Location of retrieved locations
        print("Place: ",y[i]['formatted_address'], " Location:", y[i]['geometry']['location']['lat'], " ", y[i]['geometry']['location']['lng'])

def findCityCenter():
    # keywords to filter results to gather from query search
    query = "Ankara"

    # get a query of google map search using a dictionary url and application secret key for authorization
    r = rq.get(url + 'query=' + query + '&key=' + api_key)

    # get information of data from a list of results as array of strings
    y = r.json()['results']

    # print("Format: ", y[0],"\n") -> The list of query columns: formatted_address, geometry(lat,lng),
    # viewport(northeast(lat,lng)), northwest(lat,lng), icon, id, name,
    # photos(height,html_attributions,photo_reference,width), place_id, reference, types, political

    # Print name and Location of retrieved locations
    print("Target Place: ",y[0]['formatted_address'], " Location:", y[0]['geometry']['location']['lat'], " ", y[0]['geometry']['location']['lng'])

    return y[0]['geometry']['location']

def findMyPlace():

    # keywords to filter results to gather from query search
    query = 'me'

    # get a query of google map search using a dictionary url and application secret key for authorization
    r = rq.get(url + 'query=' + query + '&key=' + api_key)

    # get information of data from a list of results as array of strings
    y = r.json()['results']

    # print("Format: ", y[0],"\n") -> The list of query columns: formatted_address, geometry(lat,lng),
    # viewport(northeast(lat,lng)), northwest(lat,lng), icon, id, name,
    # photos(height,html_attributions,photo_reference,width), place_id, reference, types, political

    # Fornat: "My Place: ",y[0]['formatted_address'], " Location:", y[0]['geometry']['location']['lat'], " ", y[0]['geometry']['location']['lng'])

    return geocoder.ipinfo('me').latlng

# find a location with latitude and longitude parameters
def findLocationWhere():

    print("Enter your coordinates:\n")

    print("Latitude(-90 to 90): ",end="")
    lat = float(input())

    print("\nLongitude(-180 to 180): ",end="")
    lng = float(input())

    if (lat>90 or lat<-90) or (lng>180 or lng<-1180):
        print("invalid location")
        return False


    print()

    # latitude, longitude and zoom
    map.marker(lat, lng, color = random.choice(markerArr))

    # get an address from query using location parameters,
    # if api key is not set, request will be denied by GoogleCloud Platform
    query = geocoder.google([lat, lng], method='reverse', key=api_key)

    print("Locations:")
    for i in query:

        print(i)

    return True

# find the distance between current location and the city center
def findDistanceMe2City():
    
    # show your place via the device's location
    myLoc = findMyPlace() 
    targetLoc = findCityCenter()
    
    print()
    
    distanceBetween((myLoc[0],myLoc[1]),(targetLoc['lat'],targetLoc['lng']))

    map.marker(myLoc[0],myLoc[1], color = random.choice(markerArr))
    map.marker(targetLoc['lat'],targetLoc['lng'], color = random.choice(markerArr))

# calculate the radius of earth based on the current location
def findRadius (latitude):
    
    # convert latitude to radian
    latitude = math.radians(latitude)

    # Radius at sea level at equator and poles
    sea = 6378.137
    pole = 6356.752

    # calcuate the radius
    c = (sea**2 * math.cos(latitude))**2
    d = (pole**2 * math.sin(latitude))**2
    e = (sea * math.cos(latitude))**2
    f = (pole * math.sin(latitude))**2

    return math.sqrt((c+d)/(e+f))

# show the distance current location - earth core
def findDistanceMe2EarthCenter():
    myloc = findMyPlace()[0]
    print("The distance to earth center: ",findRadius(myloc))

# show the distance among two locations
def distanceBetween(loc1, loc2):

    print("Distance: ",great_circle(loc1, loc2))

# menu to examine thefeatures
def options():
    
    # prepare
    print("--Welcome to the CS458 Project--")
    ask = "y"
    
    # ask and proceed
    while input!="0" and ask=="y":

        print("Options(1,2,3):\n1)Enter coordinates of a city\n2)Show nearest distance to the city center\n3)Distance to earth center\n")
        print("Enter your option: ",end="")
        str = input()

        print()

        if str=="1":
            flag = findLocationWhere()
            if flag==True:
                map.draw("my_map.html")
                webbrowser.open("my_map.html")
        elif str=="2":
            findDistanceMe2City()
            map.draw("my_map.html")
            webbrowser.open("my_map.html")
        elif str=="3":
            findDistanceMe2EarthCenter()

        # repeat condition
        print("\nDo you wanna continue?(y/n): ", end="")
        ask = input()

        print()


# google map api prerequisites
map = gp.GoogleMapPlotter(findMyPlace()[0],findMyPlace()[1], 3)
map.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
map.apikey = api_key

# Show What We Have Got!!!
options()

# Bye
print("Arrivederci!")