#!/usr/bin/env python3
# -*- coding: utf8 -*-

import math

# Let's suppose euclidean distance because projections are a pain in the ass
haversine = lambda lat1, lng1, lat2, lng2: math.sqrt( (lat1-lat2)*(lat1-lat2) + (lng1-lng2)*(lng1-lng2))

COVERAGE_LIMIT = 0.2


#
# Input data
#
locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02}
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
    {'id': 'S8', 'lat': 45.34, 'lng': 10.94, 'enabled': False},
]


#
# Python dict to objects
#
from collections import namedtuple
def dict2obj(dicts):
    for d in dicts:
        yield namedtuple("Obj", d.keys())(*d.values())


locations = list(dict2obj(locations))
shoppers = list(dict2obj(shoppers))


#
# Coverage generator
#
def get_coverage(shoppers: list, locations: list):

    #  Iterate over the shopers
    for shp in shoppers:

        # Skip not enabled shopers
        if not shp.enabled:
            continue

        coverage = 0

        # Iterate over the locations for each shopper
        for loc in locations:

            # Get the distance
            dist = haversine(shp.lat, shp.lng, loc.lat, loc.lng)

            if dist < COVERAGE_LIMIT:
                coverage+=1

        # Yield the shoper
        yield {'shopper_id':shp.id, 'coverage': int( 100 * coverage / len(locations) ) }



if __name__ == "__main__":
    
    print("Calculating coverage")

    # Generator to list
    coverage = list(get_coverage(shoppers, locations))

    # Sort
    coverage.sort(key = lambda x: x['coverage'], reverse = True) 

    # TODO: Coverage is a list of dicts, for consistence they should be also objects
    for c in coverage:
        print(c)
