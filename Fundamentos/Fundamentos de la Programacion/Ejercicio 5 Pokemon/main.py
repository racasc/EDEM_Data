import pandas as pd

#CSV
pokemon_df = pd.read_csv('pokemon_data.csv', dtype = {"Name": str, "Type 1": str, "Speed": int, "Generation": str})

#execl

#pokemon_df_excel = pd.read_excel ("pokemon_data.xlsx")

#TXT con tabulacion

#pokemon_df_txt = pd.read_csv ("pokemon_df_txt", delimiter "\t")


#imprimir los primeros 5
#print(pokemon_df.head(5))


#imprimir los ulimos 5
#print(pokemon_df.tail(5))

#como obtenemsos los nombres de la columnas
#print(pokemon_df.columns)

'''

#obtener todos los valores de una columna pero solo de name 
nombre = pokemon_df ["Name"]
print(nombre)

'''
'''

#Obtener todos los nombres y velocidades
nombre_velocidad = pokemon_df [["Name", "Speed"]]
print(nombre_velocidad)

'''

'''
#los primeros 5 nombres
nombre_c = pokemon_df["Name"]
print(nombre_c[0:5])
'''

'''
#obtener filas
print("Fila1: ")
print (pokemon_df.iloc[0])
'''

'''

#obtener varias filas

print ("Fila 0 hasta 3: ")
print (pokemon_df.iloc[0:4])

'''

'''

#obtener todo el nombre de la fila 1

print(pokemon_df.iloc[0][1])
print (pokemon_df.iloc[10,1])
'''

'''

#iterar por todos y mostrar el indice y nombre de cada

for i, pokemon in pokemon_df.iterrows():
    print(i, pokemon ["Name"])

'''
'''
#imprimir todos los pokemos que sean de agua y de tipo 1

print(pokemon_df.loc[pokemon_df["Type 1"] == "Water"])
'''

'''

#estadisticas

print(pokemon_df.describe())

'''

''''
#Ordenacion

print(pokemon_df.sort_values ("Name", ascending=True))

'''

'''

#ordenacion mas compleja

print(pokemon_df_csv.sort_values(['Type 1','HP'], ascending=[True, False])[['Name','Type 1','HP']])

'''


#crear una columna extra calculada

pokemon_df["Total"] = pokemon_df["HP"] + pokemon_df["Attack"] + pokemon_df["Defense"] + pokemon_df["Speed"]

print(pokemon_df ["Total"])

print(pokemon_df.sort_values("Total", ascending = False).head(5)[["Name", "Total"]