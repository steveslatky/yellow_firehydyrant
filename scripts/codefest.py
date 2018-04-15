# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:18:36 2018

@author: Farheen Zehra
"""

import googlemaps

def geocode(address):
    gmaps = googlemaps.Client(key="AIzaSyDx9ajo9RB833gTJzpLwZCI1TwvSww_Ywo")
    return gmaps.geocode(address)


def get_geo_cords(address):
    json = geocode(address)
    lng = json[0]["geometry"]["viewport"]["southwest"]["lng"]
    lat = json[0]["geometry"]["viewport"]["southwest"]["lat"]
    return lng, lat

def get_lat(address):
    lng, lat = get_geo_cords(address)
    return lat


def get_lng(address):
    lng, lat = get_geo_cords(address)
    return lng

    
result = geocode("3400 lancaster avenue, Philadelphia, PA")

print(result)

print(get_geo_cords("3400 lancaster avenue, Philadelphia, PA"))