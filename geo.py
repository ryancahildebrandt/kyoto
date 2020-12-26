#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:53:20 2020

@author: ryan
"""

# %% Doc setup
import folium

from readin import restaurants, stations
from voronoi import vor_gdf

# %% Base
m = folium.Map(
	location=[34.9858, 135.7588],
	zoom_start=12,
	tiles="Stamen Toner")

# %% Restaurants
for p in range(0,len(restaurants)):
	folium.Marker(
		[restaurants['Lat'].iloc[p],
		restaurants['Long'].iloc[p]],
		tooltip=folium.Tooltip(
			restaurants['JapaneseName'].iloc[p]+"("+restaurants['Name'].iloc[p]+")"+" near "+restaurants['Station'].iloc[p]+" station, a"+"<br>"+
			restaurants['FirstCategory'].iloc[p]+" & "+restaurants['SecondCategory'].iloc[p]+" restaurant with a "+str(restaurants['TotalScore'].iloc[p])+" out of 100 score "+"<br>"+
			"and a dinner price around "+restaurants['DinnerPrice'].iloc[p]
			),
		icon = folium.Icon(icon='cutlery',color='lightgray', prefix='fa')
		).add_to(m)

# %% Stations
for s in range(0,len(stations)):
	folium.Marker(
		[stations['lat'].iloc[s],
		stations['long'].iloc[s]],
		tooltip=folium.Tooltip(
			stations['name'].iloc[s]+" Station"
			),
		icon = folium.Icon(icon='subway',color='black', prefix='fa')
		).add_to(m)

# %% Voronoi
folium.Choropleth(
	geo_data=vor_gdf,
	fill_color='#ff8c8c',
	fill_opacity = 0.5,
	line_weight=1.2,
	line_color='#ffffff',
	highlight=True,
	legend_name = "Station Regions"
	).add_to(m)

# %% Export
folium.LayerControl().add_to(m)
m.save("testmap.html")


