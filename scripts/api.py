import googlemaps
import unittest

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


def _km_to_mi(km):
    conv_fac = 0.621371
    return km * conv_fac


def get_distance():
    pass


class TestStringMethods(unittest.TestCase):
    def test_geo_cord(self):
        self.assertEqual(get_geo_cords("3400 lancaster avenue, Philadelphia, PA"),
                         (-75.1931246302915, 39.9557470197085))

    def test_get_distance(self):
        self.asserEquals(True,False)

result = geocode("3400 lancaster avenue, Philadelphia, PA")

print(result)

print(get_geo_cords("3400 lancaster avenue, Philadelphia, PA"))


if __name__ == '__main__':
    unittest.main()
    # geocode("3400 lancaster avenue, Philadelphia, PA")


