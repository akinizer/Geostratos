import googlemaps, requests as rq, json, pandas as pd, numpy as np, geocoder, os, geopy, math
from geopy.distance import great_circle

from datetime import datetime

api_key = 'AIzaSyCoyLKNRnhMJZCMz7DCkwUnlipIRU88_zU'
os.environ["GOOGLE_API_KEY"] = api_key

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
    # url of the text search dictionary
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # keywords to filter results to gather from query search
    query = 'here'

    # get a query of google map search using a dictionary url and application secret key for authorization
    r = rq.get(url + 'query=' + query + '&key=' + api_key)

    # get information of data from a list of results as array of strings
    y = r.json()['results']

    # print("Format: ", y[0],"\n") -> The list of query columns: formatted_address, geometry(lat,lng),
    # viewport(northeast(lat,lng)), northwest(lat,lng), icon, id, name,
    # photos(height,html_attributions,photo_reference,width), place_id, reference, types, political

    # keep looping up to length of y

    print("My Place: ",y[0]['formatted_address'], " Location:", y[0]['geometry']['location']['lat'], " ", y[0]['geometry']['location']['lng'])

    return y[0]['geometry']['location']


def findLocationWhere():

    print("Enter your coordinates:\n")

    print("Latitude(0 to 90): ",end="")
    lat = input()

    print("\nLongitude(0 to 180: ",end="")
    lng = input()

    print()

    # get an address from query using location parameters,
    # if api key is not set, request will be denied by GoogleCloud Platform
    query = geocoder.google([lat, lng], method='reverse', key=api_key)

    print("Locations:")
    for i in query:
        print(i)

def findDistanceMe2City():
    myLoc = findMyPlace() # show your place via the device's location
    targetLoc = findCityCenter()
    print()
    distanceBetween((myLoc['lat'],myLoc['lng']),(targetLoc['lat'],targetLoc['lng']))

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

def findDistanceMe2EarthCenter():
    myloc = findMyPlace()['lat']
    print("The distance to earth center: ",findRadius(myloc))

def distanceBetween(loc1, loc2):

    print("Distance: ",great_circle(loc1, loc2))

def options():
    print("--Welcome to the CS458 Project--")
    str = ""
    ask = "y"
    while input!="0" and ask=="y":
        print("Options(1,2,3):\n1) Enter coordinates of a city\n2)Show nearest distance to the city center\n3)Distance to earth center\n")

        print("Enter your option: ",end="")
        str = input()

        print()

        if str=="1": findLocationWhere()
        elif str=="2": findDistanceMe2City()
        elif str=="3": findDistanceMe2EarthCenter()
        print("\nDo you wanna continue?(y/n): ", end="")
        ask = input()

        print()

options()