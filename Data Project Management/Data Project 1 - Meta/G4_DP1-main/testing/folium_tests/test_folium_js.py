""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""
import random
import time
from datetime import datetime

import pandas as pd
from faker import Faker
from flask import Flask
from testing.map_utils import get_df
import folium

app = Flask(__name__)


@app.route('/')
def index():
    # start_coords = (46.9540700, 142.7360300)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    # return folium_map._repr_html_()
    while True:
        df = get_df()
        folium_map = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=14, control_scale=True)
        for index, df_info in df.iterrows():
            folium.Marker([df_info["lat"], df_info["lon"]], popup=df_info["name"]).add_to(folium_map)

        folium_map._repr_html_()

        # start_coords = (46.9540700, 142.7360300)
        # folium_map = folium.Map(location=start_coords, zoom_start=14)
        # return folium_map._repr_html_()



if __name__ == '__main__':
    while True:
        app.run(debug=True)
        time.sleep(1)
        print('CAMBIO')