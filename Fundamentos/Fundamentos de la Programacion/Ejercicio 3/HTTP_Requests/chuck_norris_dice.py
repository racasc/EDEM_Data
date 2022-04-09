#Archivo chuck_norris_dice.py
import requests 
def obtenerChiste():   

  # URL -> api-endpoint  
  URL = 'https://api.chucknorris.io/jokes/random'   
  respuesta = requests.get(url = URL)

  # Extraemos los datos en formato JSON
  datos = respuesta.json()
 
  # Obtenemos valor en la clave 'value' del JSON que nos interesa
  frase_chuck: str = datos['value']
  # Imprimimos el chiste por consola 
  print (f'****CHISTECITO****')
  print(frase_chuck)


