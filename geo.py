#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:53:20 2020

@author: ryan
"""

#%% Doc setup
#from readin import restaurants
import geoplot as gplt
import geopandas as gpd
import folium

#%%

m = folium.Map(location=[34.9858, 135.7588],
	zoom_start=12)
m.save("testmap.html")
