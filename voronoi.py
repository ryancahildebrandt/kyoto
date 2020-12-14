#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 6 11:18:51 2020

@author: ryan
"""

# %% Doc setup
import geopandas as gpd
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapely

from matplotlib.patches import CirclePolygon
from readin import max_lat, max_lon, min_lat, min_lon, restaurants, stations
from scipy.spatial import ConvexHull, Voronoi, convex_hull_plot_2d, voronoi_plot_2d
from shapely.geometry import LineString, MultiPoint, MultiPolygon, Point, Polygon
from shapely.ops import cascaded_union
from shapely.ops import polygonize, unary_union



# %% Voronoi
stations_points = list(zip(stations['long'], stations['lat']))
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



# %% Boundary




restaurants_points = list([(i,j) for i, j in zip(list(restaurants.Long), list(restaurants.Lat))])
all_points = restaurants_points+stations_points
all_points_hull = ConvexHull(all_points)
boundary_points= all_points_hull.points




