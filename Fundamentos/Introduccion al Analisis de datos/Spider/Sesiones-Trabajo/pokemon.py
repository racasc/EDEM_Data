# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:22:34 2021

@author: rcasa
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())

pok = pd.read_csv ("All_Pokemon.csv", sep= ",", decimal = ".")
print(pok.Mean.describe())

x=pok.Mean

plt.hist(x,edgecolor="black", bins=20)
plt.xticks(np.arange(0, 150, step=10))#xticks: define los ticks de la eje de la x
plt.title("Figura 1, Estadisticas de combate de Pokemons")
plt.ylabel("Pokemons")
textstr = "n= 1032 \nMean= 73.10 \nstd= 20.11"
props = dict(boxstyle='round', facecolor= "white", lw=0.5)
plt.text(100, 140, textstr, bbox=props)
plt.axvline(x=73.10, linewidth=1, linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=55, linewidth=1, linestyle= 'dashed',color="green", label='Mean')
plt.axvline(x=85.83, linewidth=1, linestyle= 'dashed',color="green", label='Mean')



plt.show()

poke = pd.read_csv ("All_Pokemon.csv", sep= ",", decimal = ".")

mytable = poke.groupby(["Generation"]).size()
print(mytable)

bar_list = ["1", "2","3","4","5","6","7","8"]
plt.bar(bar_list, mytable)
plt.title("Figura 2, Numero de Pokemons en cada generación")
plt.ylabel("Pokemons")
plt.xlabel("Generación")


