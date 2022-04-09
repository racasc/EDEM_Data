# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:56:57 2021

@author: rcasa
"""

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 
from scipy.stats.stats import pearsonr
from statsmodels.formula.api import ols

# Change working directory
os.chdir('C:\EDEM\PEP\code_and_data')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK


#histograma de la temperatura
x=wbr["temp_celsius"]
plt.hist(x,bins=10, edgecolor="black")



#scatter plot
plt.figure(figsize=(5,5))
plt.scatter (wbr.temp_celsius, wbr.cnt, s=20, facecolors="none", edgecolors="C0")
plt.xlabel("Temperatura")
plt.ylabel("Daily rentals")


#correlation
from scipy.stats.stats import pearsonr
x= wbr.temp_celsius
y=wbr.cnt

pearsonr (x,y)
#(0,62 es la correlacion y el 2.81... es el pvalue)

r, p_val = pearsonr(x,y)

print(r,p_val)
n = len(wbr.cnt)
print('r:', round(r,3), 'P.Val:', round(p_val,3), 'n:', n)


#esto es un grafico wapo
plt.figure(figsize=(5,5))
x= wbr.temp_celsius
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", edgecolors="C0")
plt.xticks(np.arange(0,40,step=5))
plt.yticks(np.arange(0,10000,step=1000))
plt.title("Figure 9. Daily bi¡icyle rentals by temperature")
plt.ylabel("Daily Rentals")
plt.xlabel("Temperature Cº")
props =dict(boxstyle ="round", facecolor ="white", lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)


#esto es un grafico wapo cambiado el color por los años
plt.figure(figsize=(5,5))
x= wbr.temp_celsius
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", c=wbr.yr)
plt.xticks(np.arange(0,40,step=5))
plt.yticks(np.arange(0,10000,step=1000))
plt.title("Figure 9. Daily bi¡icyle rentals by temperature")
plt.ylabel("Daily Rentals")
plt.xlabel("Temperature Cº")
props =dict(boxstyle ="round", facecolor ="white", lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)

#esto es un grafico wapo cambiado el color por los seasons
plt.figure(figsize=(5,5))
x= wbr.temp_celsius
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", c=wbr.season)
plt.xticks(np.arange(0,40,step=5))
plt.yticks(np.arange(0,10000,step=1000))
plt.title("Figure 9. Daily bi¡icyle rentals by temperature")
plt.ylabel("Daily Rentals")
plt.xlabel("Temperature Cº")
props =dict(boxstyle ="round", facecolor ="white", lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)



#######################################################################
#windspeed correlation
from scipy.stats.stats import pearsonr
x= wbr.windspeed_kh
y=wbr.cnt

pearsonr (x,y)
#(0,62 es la correlacion y el 2.81... es el pvalue)

r, p_val = pearsonr(x,y)

print(r,p_val)
n = len(wbr.cnt)
print('r:', round(r,3), 'P.Val:', round(p_val,3), 'n:', n)


plt.figure(figsize=(5,5))
x= wbr.windspeed_kh
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", edgecolors="C0")
plt.xticks(np.arange(0,40,step=5))
plt.yticks(np.arange(0,10000,step=1000))
plt.title("Figure 10. Daily bicycle rentals by windspeed")
plt.ylabel("Daily Rentals")
plt.xlabel("Windspeed")
props =dict(boxstyle ="round", facecolor ="white", lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (25,7000, textstr , bbox=props)

# =============================================================================
#Sesion 10 
# =============================================================================
#histograma
wbr.cnt.hist()
wbr.temp_celsius.hist()

#scatter
plt.figure(figsize=(5,5))
x= wbr.temp_celsius
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", edgecolors="C0")


#ecuacion de la recta que busque una nueva recta

from statsmodels.formula.api import ols

#OLS = ordinary least squares

#Regression
model1= ols("cnt ~ temp_celsius", data=wbr).fit()
print(model1.summary2())

# Intercept: cuando la variable predictora vale 0, donde empiezaria la variable target.
# temp_celsius: cuanto se incremtna la variable target (dependiente), por cada incremento en una unidad de la variable predictora 
#el p value del intercept no lo vamos a intrepetar
#el p value de la variable independiente es la que nos interesa
    # la pendiente que vemos en una muestra, con un valor menor al 0.05, tiene sentido

#rsquared: que porcentaje de la variabilidad del fenomeno se puede saber con solo una variable


wbr.windspeed_kh.hist()
plt.figure(figsize=(5,5))
x= wbr.windspeed_kh
y=wbr.cnt
plt.scatter (x, y, s=20, facecolors="none", edgecolors="C0")


model1b= ols("cnt ~ windspeed_kh", data=wbr).fit()
print(model1b.summary2())

#Regresion multiple
model2= ols("cnt ~ temp_celsius + windspeed_kh", data=wbr).fit()
print(model2.summary2())

model3= ols("cnt ~ temp_celsius + windspeed_kh + hum", data=wbr).fit()
print(model3.summary2())

model4= ols("cnt ~ temp_celsius + windspeed_kh + hum + workingday", data=wbr).fit()
print(model4.summary2())

model5= ols("cnt ~ temp_celsius + windspeed_kh + hum + yr", data=wbr).fit()
print(model5.summary2())

#el dia en que la temperatura valga 0, el veinto valga 0, la humedad valga 0 y el año para 0 (2011), esperas vender 2593
#si incremeto la temperatura un grado mas, vendo 153 bicis mas
#por cada incremento que hago es de 2006 bicis

#pasar de 0 a 1, vender 2006 bicis mas

#unacimante podemos inclur variables dicotomicas 




























