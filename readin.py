#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:17:51 2020

@author: ryan
"""

# Doc setup
import math
import pandas as pd

# Max & Min

max_lon = 135.8183
min_lon = 135.672
max_lat = 35.07
min_lat = 34.920

# Kyoto Restaurant Info

restaurants = pd.read_csv("./data/Kyoto_Restaurant_Info.csv")
restaurants = restaurants[(restaurants['Lat'].between(min_lat, max_lat)) & (restaurants['Long'].between(min_lon, max_lon))]
restaurants["Station"] = restaurants.Station.replace("Sai", "Saiin").replace("Arashiyama Torokko Station", "Arashiyama Torokko")
restaurants["SecondCategory"] = restaurants["SecondCategory"].fillna("None")

# Station Info

stations = pd.DataFrame()
stations["name"] = restaurants.Station.unique()
stations["lat"] = [34.9858, 35.0037, 35.0087, 34.9956, 35.0109, 35.0038, 35.004, 35.0094, 35.01, 35.0033, 35.0121, 35.0024, 34.9959, 35.0169, 34.9738, 35.0094, 34.9954, 35.0033399, 34.9924, 34.9794, 34.9644, 34.932, 34.9326, 35.0186, 35.0383, 35.0108, 35.0032, 35.0305, 34.96765, 34.9569, 35.0274, 35.0109, 35.018, 34.9799, 34.9269, 34.9898, 35.0181, 35.0452, 34.9645, 35.0502, 35.0102, 34.9796, 35.0298, 34.9922, 35.0378, 35.0111, 35.008, 34.9539, 35.035, 34.9727, 35.0516, 35.0513, 34.9816, 34.9248, 34.981, 35.0264, 35.0441, 34.9333762, 35.0171354, 35.0083, 34.9235, 34.9551, 35.0633] 
stations["long"] = [135.7588, 135.7606, 135.7727, 135.7424, 135.7681, 135.7687, 135.7721, 135.7723, 135.7596, 135.7316, 135.7505, 135.7597, 135.7686, 135.7597, 135.7524, 135.7797, 135.7597, 135.7485669, 135.8172, 135.7033, 135.7701, 135.7934, 135.7643, 135.7177, 135.7845, 135.7156, 135.7485, 135.7732, 135.76867, 135.7703, 135.7309, 135.7305, 135.7722, 135.7526, 135.7604, 135.7679, 135.7307, 135.7587, 135.7104, 135.7904, 135.6817, 135.75753, 135.7594, 135.718, 135.7593, 135.7418, 135.7321, 135.7046, 135.7815, 135.8149, 135.777, 135.7660, 135.8166, 135.6923, 135.7323, 135.7181, 135.7874, 135.763333, 135.6680884, 135.7234, 135.7008, 135.7562, 135.7852]

# Category cleanup

raw_cat_list=["Sweets","Crepes","Sweets (and others)","Bread","Shaved ice (snow cone)","Pancake","Bar","Stand Bar","Dining bar","Wine bar","Beer","Beer bar","Nihonshu (Japanese sake)","Shochu (Japanese spirits)","Lounge","Beer garden","Fowl","Genghis Khan (BBQ Rum)","Gyutan (Beef tongue)","Yakiniku (BBQ Beef)","Yakitori (Grilled chicken)","Horumon (BBQ Offel)","Kushiyaki (Grilled skewer)","Steak","Boneless deep-fried chicken","Hamburger Steak","Robatayaki","Meat dishes","Tonkatsu (Pork cutlet)","Beef dishes","BBQ","Sumibiyaki","Bento (Lunch box)","Bistro","Cafe","Coffee shoppe","Traditional Café","Café / coffee shop (and others)","Cantonese Cuisine","Dim sum","Shanghai Cuisine","Chinese hot pot / fire pot","Chinese","Sichuan Cuisine","Curry (other)","Curry rice","Thai Curry","Dumplings","Fried Foods (other)","Kushi-age (Fried Skewer)","Fugu (Blowfish)","Pork Shabu Shabu","Motsu Nabe (Offel Hot Pot)","Chanko Nabe (Sumo Wrestlers Hot Pot)","Chiritori nabe (tripe)","Mizutaki","Shabu Shabu (Japanese Steamboat)","Hot Pot (other)","Indian curry","India cuisine","Izakaya (other)","Pub","Izakaya (Tavern)","beer restaurant","Okinawan Cuisine","Japanese food (other)","Kaiseki (Traditional Japanese)","Kappo (Traditional Japanese)","Korean cuisine","Korean hot pot","Kyoto Cuisine","None","Udon","Chow Mein Noodle","Soba","Tsukemen","Standing style soba","Udon Suki","Dandan noodles","Champon Noodle","Oden","Okonomiyaki","Monjya yaki","Regional Cuisine (Other)","Other","table d'hôte","Restaurants (other)","Fusion cuisine","Innovative cuisine","Creative cuisine","Asian & ethnic cuisine (and others)","Buffet style","Oyako-don (Chicken Bowl)","Ramen","Ryokan","Indonesia cuisine","Thailand cooking","Viet Nam cuisine","Angler","Crab","Seafood","Shojin Cuisine (Buddhist Cuisine)","Sukiyaki","Suppon (Soft-shelled Turtle)","Sushi","Takoyaki","Ten-don (Tempura Bowl)","Tempura","Teppanyaki","FROM","Tofu","Yuba","Unagi (Freshwater eel)","Vegetable dishes","Western Food (Other)","European-style Curry","Pasta","Italian","Spain","Sandwich","Western Cuisine","Modern French","Mediterranean","Mexico cuisine","French","Croquette","Pizza","Western (Others)","Burger"]
cat_list=["Bakery/Sweets","Bakery/Sweets","Bakery/Sweets","Bakery/Sweets","Bakery/Sweets","Bakery/Sweets","Bar","Bar","Bar","Bar","Bar","Bar","Bar","Bar","Bar","Bar","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","BBQ/Meat","Bento","Bistro","Cafe","Cafe","Cafe","Cafe","Chinese","Chinese","Chinese","Chinese","Chinese","Chinese","Curry","Curry","Curry","Dumplings","Fried Foods","Fried Foods","Seafood","Hot Pot","Hot Pot","Hot Pot","Hot Pot","Hot Pot","Hot Pot","Hot Pot","S/E Asian","S/E Asian","Izakaya","Izakaya","Izakaya","Izakaya","Japanese","Japanese","Kaiseki","Kappo","Korean","Korean","Kyoto","No other category","Noodles","Noodles","Noodles","Noodles","Noodles","Noodles","Noodles","Noodles","Japanese","Okonomiyaki","Okonomiyaki","Other","Other","Other","Other","Other","Other","Other","Other","Other","Japanese","Ramen","Ryokan","S/E Asian","S/E Asian","S/E Asian","Seafood","Seafood","Seafood","Shojin Ryouri","Japanese","Seafood","Sushi","Japanese","Tempura","Tempura","Teppanyaki","TO","Tofu","Tofu","Seafood","Other","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western","Western"]
cat_dict= dict(zip(raw_cat_list,cat_list))

restaurants["FirstCatSimp"]=[cat_dict[i] for i in restaurants.FirstCategory]
restaurants["SecondCatSimp"]=[cat_dict[i] for i in restaurants.SecondCategory]

# Rating to Score (out of 100, rounded down)

restaurants["DinnerScore"]=[i if math.isnan(i) else math.floor(i*20) for i in restaurants.DinnerRating]
restaurants["LunchScore"]=[i if math.isnan(i) else math.floor(i*20) for i in restaurants.LunchRating]
restaurants["TotalScore"]=[i if math.isnan(i) else math.floor(i*20) for i in restaurants.TotalRating]