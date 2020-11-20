#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:17:51 2020

@author: ryan
"""

#%% Doc setup
import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#%% Kyoto Restaurant Info

restaurants = pd.read_csv("./data/Kyoto_Restaurant_Info.csv")

#%% Global Map JPN 

dat=gpd.read_file("./data/kansai-latest-free.shp/gis_osm_buildings_a_free_1.shx")
dat.plot()
plt.show()


