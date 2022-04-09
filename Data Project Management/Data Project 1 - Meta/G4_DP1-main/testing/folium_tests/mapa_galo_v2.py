#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:16:03 2022

@author: galovalle
"""

# NO TOCAR
from faker import Faker
import keyboard
import time
import random
from datetime import datetime
import pandas as pd
import folium
import webbrowser


faker = Faker('es_ES')
USERS_TOTAL=5
users={}
lat_min=39.4
lat_max=39.5
lon_min=-0.3
lon_max=-0.4
vehicles=["Bike","Train","Car", "Walking"]

def initiate_data():
    global users
    for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        user["friends"]=[]
        user["position"]={"lat":random.uniform(39.4, 39.5),"lon":random.uniform(-0.3, -0.4)}
        user["age"]=random.uniform(16, 85)
        user["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user   
        print(user)
    num=0
    for element in users.items():
        print(f"Generating friends of {num} of {len(users)}")
        for i in range(0,random.randint(1,10)):
            friend=random.choice(list(users.values()))
            if friend["id"]!=element[0]:
                users[element[0]]["friends"].append(friend["id"])
            else:
                print("No friend of yourself") 
        num=num+1

    print("DATA GENERATED")        


def generate_step():
    global users
    if len(users)>0:
        print("STEP")
        for element in users.items():
            users[element[0]]["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            lat=users[element[0]]["position"]["lat"]
            lon=users[element[0]]["position"]["lon"]
            users[element[0]]["position"]["lon"]=lon+random.uniform(0.001, 0.005)
            users[element[0]]["position"]["lat"]=lat+random.uniform(0.001, 0.005)
            if lat>lat_max or lat<lat_min:
                users[element[0]]["position"]["lat"]=random.uniform(39.4, 39.5)
                users[element[0]]["transport"]=random.choice(vehicles)
            if lon>lon_max or lon<lon_min:
                users[element[0]]["position"]["lon"]=random.uniform(-0.3, -0.4)
            
    else:
        initiate_data()
    return users



# NO TOCAR

while True:
    try:  
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Exited the data generator')
            break  
        else:
            users_generated=generate_step()
            # Place your code here
            #Generamos una lista con las claves del diccionario para pode iterar
            claves =users.keys()
            listaclaves=list(claves)

            #Creamos un DataFrame para poder iterar en la función folium

            df = pd.DataFrame()
            df['lat'] = None
            df['lon'] = None
            df['name'] = None

            for i in range (0,USERS_TOTAL):
              a=listaclaves[i]
              df.loc[i+1]=[users[a]['position']['lat'], users[a]['position']['lon'],users[a]['name']]

            #Generamos el mapa mediante la función folium
              
            map = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=14, control_scale=True)
            for index, df_info in df.iterrows():
                folium.Marker([df_info["lat"], df_info["lon"]], popup=df_info["name"]).add_to(map)

            map.save('mapa.html')
            webbrowser.open('mapa.html',new=0)
            print("code")
            # End Place for code
            time.sleep(2)
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        break  