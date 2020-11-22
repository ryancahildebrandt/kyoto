#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:53:20 2020

@author: ryan
"""

#%% Doc setup
import folium
import geopandas as gpd
import geoplot as gplt

from readin import restaurants

#%%

m = folium.Map(
	location=[34.9858, 135.7588],
	zoom_start=11,
	tiles="Stamen Toner")

loc_list = restaurants[["Lat" , "Long"]].values.tolist()
for p in loc_list:
    folium.Marker(p).add_to(m)

m.save("testmap.html")
