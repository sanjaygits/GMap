# Author    : Sanjay Kumar
# Purpose   : Edureka Python Self Paced Course Project.
#             Q2: Create a script called location that return the location parameters of any location you want.
# Date      : 14 Feb 2018


import googlemaps
from datetime import datetime
import json
from pprint import pprint

#My Google API Key. 
gmaps = googlemaps.Client(key='AIzaSyDC7hNFXWum48OYliVbKbH0RAIPGieejDA')

#Get the location for which the cordinates are required.
location = input('Enter a location to find its cordinates: ')

#use the geocode() to get the detailed information about the location.
geocode_result = gmaps.geocode(location)

#For debugging.
#pprint(geocode_result[0]['geometry']['location']['lat'])
#print(geocode_result[0]['geometry']['location']['lng'])

if(geocode_result==[]):
    print("Error. No such location found.")
else:
    #pprint(geocode_result)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    print("The cordinates of {} are \nLatitude = {} \nLongitude = {}".format(location, latitude, longitude))

    






