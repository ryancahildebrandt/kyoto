#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:00:43 2020

@author: ryan
"""

# Doc setup
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sidetable as stb 

from readin import restaurants
from readin import stations
from shapely.geometry import MultiPoint
from shapely.geometry import Point
from shapely.geometry import mapping
from shapely.ops import nearest_points
from voronoi import restaurants_points
from voronoi import stations_points

# Calculate Nearest Station

def get_nearest_station(poi=Point(restaurants_points[0])):
	stations_mp=MultiPoint(stations_points)
	testpoint=Point(nearest_points(poi, stations_mp)[0])
	soi=restaurants.Station[(restaurants.Lat==testpoint.y) & (restaurants.Long==testpoint.x)]
	soi=list(soi)[0]
	return(soi)

restaurants["Nearest"]=[get_nearest_station(Point(restaurants_points[i])) for i in range(len(restaurants.Name))]

# Split and Export Stbs

for station in restaurants.Nearest.unique():
	name=station.replace(" ", "_")
	exec(f"{name}_df = restaurants[restaurants.Nearest==station]")
	exec(f"{name}_stb_cat_1 = {name}_df.stb.freq(['FirstCatSimp'])")
	exec(f"{name}_stb_cat_2 = {name}_df.stb.freq(['SecondCatSimp'])")
	exec(f"{name}_stb_cat_12 = {name}_df.stb.freq(['FirstCatSimp','SecondCatSimp'])")
	exec(f"{name}_stb_price_d = {name}_df.stb.freq(['DinnerPrice'])")
	exec(f"{name}_stb_price_l = {name}_df.stb.freq(['LunchPrice'])")
	exec(f"{name}_stb_score_d = {name}_df.stb.freq(['DinnerScore'])")
	exec(f"{name}_stb_score_l = {name}_df.stb.freq(['LunchScore'])")
	exec(f"{name}_stb_score_t = {name}_df.stb.freq(['TotalScore'])")
	exec(f"{name}_stb_score_price_d = {name}_df.stb.freq(['DinnerScore','DinnerPrice'])")
	exec(f"{name}_stb_score_price_l = {name}_df.stb.freq(['LunchScore','LunchPrice'])")
	exec(f"{name}_stb_cat1_price_d = {name}_df.stb.freq(['FirstCatSimp','DinnerPrice'])")
	exec(f"{name}_stb_cat1_price_l = {name}_df.stb.freq(['FirstCatSimp','LunchPrice'])")
	exec(f"{name}_full = pd.concat([{name}_stb_cat_1,{name}_stb_cat_2,{name}_stb_cat_12,{name}_stb_price_d,{name}_stb_price_l,{name}_stb_score_d,{name}_stb_score_l,{name}_stb_score_t,{name}_stb_score_price_d,{name}_stb_score_price_l,{name}_stb_cat1_price_d,{name}_stb_cat1_price_l], ignore_index=True)")
	exec(f"{name}_full = {name}_full[['count','percent','FirstCatSimp','SecondCatSimp','DinnerPrice','LunchPrice','DinnerScore', 'LunchScore', 'TotalScore']]")
	exec(f"{name}_full.to_csv('./data/{name}_full.csv')")

station_groupby_df=restaurants[["Station","TotalScore"]].groupby("Station").describe()

# Izakaya 

izakaya_df = restaurants[restaurants.FirstCatSimp=="Izakaya"]
izakaya_df.to_csv('./data/izakaya_df.csv')
izakaya_df.stb.freq(["SecondCatSimp"])
izakaya_df.stb.freq(["DinnerPrice"])
izakaya_df.stb.freq(["LunchPrice"])
izakaya_df.stb.freq(["DinnerScore"])
izakaya_df.stb.freq(["LunchScore"])
izakaya_df.stb.freq(["TotalScore"])
izakaya_df.stb.freq(["Station"])

