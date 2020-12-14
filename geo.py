#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:53:20 2020

@author: ryan
"""

# %% Doc setup
import folium
import geopandas as gpd
import geoplot as gplt
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from readin import restaurants, stations
from voronoi import all_points, all_points_hull, boundary_points, boundary_polygon, vorGeoJSON

# %%

m = folium.Map(
	location=[34.9858, 135.7588],
	zoom_start=12,
	tiles="Stamen Toner")

for p in range(0,len(restaurants)):
	folium.Marker(
		[restaurants['Lat'].iloc[p],
		restaurants['Long'].iloc[p]],
		tooltip=folium.Tooltip(
			[restaurants['JapaneseName'].iloc[p],
			restaurants['Lat'].iloc[p],
			restaurants['Long'].iloc[p]])
		).add_to(m)

for s in range(0,len(stations)):
	folium.Marker(
		[stations['lat'].iloc[s],
		stations['long'].iloc[s]],
		tooltip=folium.Tooltip(
			[stations['name'].iloc[s],
			stations['lat'].iloc[s],
			stations['long'].iloc[s]]),
		icon = folium.Icon(color='red')
		).add_to(m)

folium.Choropleth(
	geo_data=json.dumps(vorGeoJSON),
#	fill_color='#00704A',
	fill_opacity = 0.5,
	line_weight=0.8,
#	line_color="#008800",
	highlight=True,
	legend_name = "Station Regions"
	).add_to(m)

folium.GeoJson(
	boundary_polygon
	).add_to(m)


folium.LayerControl().add_to(m)

m.save("testmap.html")


