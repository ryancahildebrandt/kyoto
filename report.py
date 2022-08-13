#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:02:09 2020

@author: ryan
"""

# Doc setup
import datapane as dp
import sidetable as stb

from geo import m
from profiles import Arashiyama_df
from profiles import Chayama_df
from profiles import Demachiyanagi_df
from profiles import Hanazono_df
from profiles import Kokusaikaikan_df
from profiles import izakaya_df
from profiles import restaurants
from profiles import station_groupby_df

# Report

rprt = dp.Report(
	dp.Text("""
# 京都, in Stations and Their Restaurants
### Exploration of restaurants in Kyoto and the stations they're closest to
Splitting up Kyoto restaurants by regions centered on train/subway stations, as well as checking out some interesting characteristics of the different restaurants near each station. As it turns out, there's a ton of izakaya in the city
---
"""),
	dp.Plot(m),
	dp.Text("""
## Dataset
The dataset used for the current project can be found [here](https://www.kaggle.com/koki25ando/tabelog-restaurant-review-dataset). Station data was pulled manually from wikipedia and google maps.
"""),
	dp.DataTable(restaurants),
	dp.Text("""
## Some Special Station Profiles
*Taking a look at some stations which have interesting or peculiar restaurant selection*
"""),
	dp.DataTable(station_groupby_df),
	dp.Text("""
### Arashiyama
#### Lots (relatively, at least) of tofu options, beware of expensive lunch prices
		"""),
	dp.DataTable(Arashiyama_df),
	dp.Text("""
### Demachiyanagi
#### A station whose food options are split between expensive kaiseki and cheap izakaya fare
		"""),
	dp.DataTable(Demachiyanagi_df),
	dp.Text("""
### Hanazono
#### Another station with polarized food options, with one shojin ryouri place and one meat-centric bbq joint
		"""),
	dp.DataTable(Hanazono_df),
	dp.Text("""
### Kokusaikaikan
#### Station with the best average restaurant rating at 70/100
		"""),
	dp.DataTable(Kokusaikaikan_df),
	dp.Text("""
### Chayama, Nishioji Oike, Nagaoka Tenjin, Uzumasa Tenjingawa, Higashi Muko, and more
#### Stations to avoid if you're looking solely for restaurant options, with the lowest average score of 60/100
		"""),
	dp.DataTable(restaurants.stb.freq(["TotalScore"])),
	dp.Text("""
## Izakaya Exploration
*Izakaya are all over Kyoto, so here's a little breakdown of where they are and what they're like*

		"""),
	dp.DataTable(izakaya_df),
	dp.Text("""
#### Stations
+ Perhaps unsurprisingly, most izakaya are centered around the stations with the most restaurants, which are also the stations closest to the central areas of Kyoto. Kyoto, Karasuma, Kawaramachi, Shijo, and Sanjo stations have the most access to just about any  izakaya you could want.
		"""),
	dp.DataTable(izakaya_df.stb.freq(["Station"])),
	dp.Text("""
#### Second Category
+ Lots of izakaya show seafood as their main fare, with meat & bbq not too far behind. Other Japanese and more generic bar fare round out the top categories of food at the majority of izakaya in Kyoto.
		"""),
	dp.DataTable(izakaya_df.stb.freq(["SecondCatSimp"])),
	dp.Text("""
#### Price
+ For lunch, it's a pretty straightforward spread of price ranges, with most falling below the ￥1000 and fewer and fewer in each higher price bracket. Dinner prices are a little more centered on the ￥3000-￥4000 bracket, with the distribution spreading out from from there pretty evenly.
		"""),
	dp.DataTable(izakaya_df.stb.freq(["LunchPrice"])),
	dp.DataTable(izakaya_df.stb.freq(["DinnerPrice"])),
	dp.Text("""
#### Rating
+ Ratings for izakaya are pretty low across the board, with the majority falling below a 65/100. There isn't much of a spread in quality, with the lowest rated izakaya falling at 60 and the highest at 71. 
		"""),
	dp.DataTable(izakaya_df.stb.freq(["TotalScore"])),
	dp.Text("""
# 完了
		""")
	)



rprt.save(path='outputs/kyoto_rprt.html', open=False)
#rprt.publish(name='Kyoto_in_Stations_and_Restaurants', open=True, visibility='PUBLIC')
#https://datapane.com/u/ryancahildebrandt/reports/kyoto-in-stations-and-restaurants