#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 6 11:18:51 2020

@author: ryan
"""

# Doc setup
import geopandas as gpd
import numpy as np

from readin import max_lat
from readin import max_lon
from readin import min_lat
from readin import min_lon
from readin import restaurants
from readin import stations
from scipy.spatial import Voronoi
from shapely.geometry import LineString
from shapely.geometry import MultiPoint
from shapely.geometry import MultiPolygon
from shapely.geometry import Point
from shapely.ops import polygonize

# Voronoi
four_corners = [
(max_lon, max_lat),
(max_lon, min_lat),
(min_lon, max_lat),
(min_lon, min_lat),
(135.66, max_lat) #an extra point, dirty fix for voronoi
]

stations_points = list(zip(stations['long'], stations['lat']))+four_corners
stations_vor = Voronoi(stations_points)

def makeGeoPolygon(vertices, region):
    if -1 in region or region == []:
        return None    
    poly = [[vertices[v][0], vertices[v][1]] for v in region]
    poly = poly + [poly[0]]
    return {"type": "Polygon", "coordinates": [poly] }

vorGeoJSON = {
    "type": "FeatureCollection",
    "features": [ {"type": "Feature", 
                   "geometry": makeGeoPolygon(stations_vor.vertices, region)} 
                 for region in stations_vor.regions if (-1 not in region) and (len(region) > 0)
                ]
}


# Boundary 
# from https://stackoverflow.com/questions/34968838/python-finite-boundary-voronoi-cells
restaurants_points = list([(i,j) for i, j in zip(list(restaurants.Long), list(restaurants.Lat))])
all_points = restaurants_points+stations_points

points = np.array(all_points)
lines = [LineString(stations_vor.vertices[line]) for line in stations_vor.ridge_vertices if -1 not in line]
pts = MultiPoint([Point(i) for i in all_points])
mask = pts.convex_hull.union(pts.buffer(.01, resolution=10, cap_style=1))
result = MultiPolygon([poly.intersection(mask) for poly in polygonize(lines)])

vor_gdf = gpd.GeoDataFrame(geometry=[i for i in result]).to_json()

