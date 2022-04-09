from datetime import datetime
import pandas as pd
import folium
import random

from faker import Faker
import altair
from IPython.display import display
import webbrowser

#Código generador de los datos

faker = Faker('es_ES')
vehicles=["Bike","Train","Car", "Walking"]
USERS_TOTAL=100
users={}
for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        user["friends"]=[]
        user["position"]={"lat":random.uniform(39.4, 39.5),"lon":random.uniform(-0.3, -0.4)}
        user["transport"]=random.choice(vehicles)
        user["age"]=random.uniform(16, 85)
        user["gender"]=random.choice(["man","woman"])
        user["weight"]=random.uniform(60, 110)
        user["height"]=random.uniform(150, 210)
        user["bodyfat"]=random.uniform(3, 45)
        user["bloodpressure_sist"]=random.uniform(120, 180)
        user["bloodpressure_diast"]=random.uniform(70, 120)
        user["cholesterol"]=random.uniform(150, 300)
        user["smoker"]=random.choice(["0","1"])
        user["drinking"]=random.uniform(0,7)
        user["disability"]=random.choice(["0","1"])
        user["previouspatology"]=random.choice(["0","1"])
        user["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user


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
        # map.save("map.html")
        # webbrowser.open("map.html")
        iframe = map._repr_html_()
        display(HTML(iframe))

exit(0)
# Incluir logo Find Me in Meta en el mapa
# Guardar logo en formato png
# Bounds = donde situar el logo, sustituir por las coordenadas de la esquina a escoger
map_image_overlay = folium.Map([latitud, longitud], zoom_start=14, control_scale=True)
img_overlay = folium.raster_layers.ImageOverlay(name='logo Grupo', image='logo_grupo.png', bounds=[[lat_min, lon_min], [lat_max, lon_max]], opacity=0.5, zindex=1)

# add image to map
img_overlay.add_to(map_img_overlay)

# display map
map_image_overlay


# Charts in Pop-Up
# si OK, mover import al principio
# dataset.head() para ver nombres columnas
altair.renderers.enable('notebook')
my_cols = pd.DataFrame({'Matchs_state': ['Match', 'No match'], 'Counter': ['nombre_columna_match', 'nombre_columna_nomatch']})
my_graph_bar = altair.Chart(my_cols, width=300).mark_bar().encode(x='Matchs_state', y='Counter'.properties(title='Match & No-match Counter'))
my_graph_bar

# folium.features.Vegalite creates a Vega-Lite chart element
vega = folium.features.VegaLite(my_graph_bar, width='100%', height='100%')

# create Popup
my_popup = folium.Popup()

# add chart to pop-up
vega.add_to(my_popup)

# add popup to map
my_popup.add_to(map)

map