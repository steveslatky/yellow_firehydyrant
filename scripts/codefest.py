# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:18:36 2018

@author: Farheen Zehra
"""

import googlemaps

def geocode(address):
    gmaps = googlemaps.Client(key="AIzaSyDx9ajo9RB833gTJzpLwZCI1TwvSww_Ywo")
    result = gmaps.geocode(address)
    return result

    
result = geocode("3400 lancaster avenue, Philadelphia, PA")
