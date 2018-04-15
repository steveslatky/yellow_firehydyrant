import googlemaps
from haversine import haversine as hs
import unittest

import googlemaps

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
    return lng, lat

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
    hs(query,input,miles)




class TestStringMethods(unittest.TestCase):
    def test_geo_cord(self):
        self.assertEqual(get_geo_cords("3400 lancaster avenue, Philadelphia, PA"),
                         (-75.1931246302915, 39.9557470197085))

    def test_get_distance(self):
        self.asserEquals(True,False)

result = _geocode("3400 lancaster avenue, Philadelphia, PA")

print(result)

print(get_geo_cords("3400 lancaster avenue, Philadelphia, PA"))


if __name__ == '__main__':
    unittest.main()
    # geocode("3400 lancaster avenue, Philadelphia, PA")


