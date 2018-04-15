import json
import sqlite3
import googlemaps
from haversine import haversine as hs
import unittest

import googlemaps

from flask import Flask
app = Flask(__name__)


'''
Input: Address -> String
Return: Json (

'''
def _geocode(address):
    gmaps = googlemaps.Client(key="AIzaSyDx9ajo9RB833gTJzpLwZCI1TwvSww_Ywo")
    return gmaps.geocode(address)


'''
Input: Address -> String
Return: Geo Coordinates of a address -> (Float, Float)

'''
def get_geo_cords(address):
    json = _geocode(address)
    lng = json[0]["geometry"]["viewport"]["southwest"]["lng"]
    lat = json[0]["geometry"]["viewport"]["southwest"]["lat"]
    return lat, lng

'''
Input: Address -> String
Return: Float

'''
def get_lat(address):
    lng, lat = get_geo_cords(address)
    return lat

'''
Input: Address -> String
Return: Float

'''
def get_lng(address):
    lng, lat = get_geo_cords(address)
    return lng

'''
Input: km -> Float
Return: miles -> Float

'''
def _km_to_mi(km):
    conv_fac = 0.621371
    return km * conv_fac


'''
Uses haversine formula to get distance with Geo coordinates

Param param input (float, float), (float, float), Optional miles=True
Return Float(miles/km) 

'''
def get_distance(query, input, miles=True):
   return hs(query,input,miles)




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None

def _db_get_geo(row):
    return (row[1],row[2])

''' Interfaces to get a list of hydrants close to an address. 

Input Address
Return: 15 closest hydrants [(Float, Float, Bool, String)] 
'''
def get_closest_hydrants(address):
    input_geo = get_geo_cords(address)

    conn = create_connection("../database/hydrants.db")
    hydrants = conn.execute("SELECT * from locations ")

    all_hydrants = hydrants.fetchall()
    dists = []
    for e,row in enumerate(all_hydrants):
        db_geo = _db_get_geo(row)
        dists.append((e,get_distance(input_geo,db_geo)))
    dists = sorted(dists, key=lambda x: x[1])
    _dists = dists[:15]
    keys = list(map(lambda x: x[0], _dists))

    print(_dists)

    f = open("../data/hydrants.json", "r")
    data_json = json.load(f)

    j
    for i in keys:
        data_json[i])

def _db_get_geo(row):
    return (row[1],row[2])

@app.route('/', methods=['GET'])
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    loc = request.args.get('location')
    closest_hydrants = get_closest_hydrants(loc)
    return closest_hydrants

