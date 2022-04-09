# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:49:11 2021

@author: rcasa
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())


rentals_2011 = pd.read_csv ("washington_bike_rentals_2011.csv", sep= ";", decimal = ",")
print(rentals_2011.shape)
print(rentals_2011.head())
print(rentals_2011.tail())

#Quality control (qc) ok

print(rentals_2011.cnt)

print(np.mean(rentals_2011.cnt))
print(np.std(rentals_2011.cnt))

print(rentals_2011.cnt.mean())
print(rentals_2011.cnt.describe())



#Las variables quantitativas: media, desviacion tipica y un histrograma


#histogram

print(plt.hist(rentals_2011.cnt))
#print(rentals_2011.cnt.hist())  #Esta no es muy buena utilizarla

#x=rentals_2011["cnt"]
x=rentals_2011.cnt #este se utiliza cuando no hay espacios en blanco

plt.hist(x,edgecolor="black", bins=20)
plt.xticks(np.arange(0, 7000, step=1000)) #xticks: define los ticks de la eje de la x
plt.title("Figure 1, Registered rentals in Washington")
plt.ylabel("Frecuencia")
plt.show()

weather_2011 = pd.read_csv ("rentals_weather_2012.csv", sep= ";", decimal = ",")
print(weather_2011.shape)
print(weather_2011.head())
print(weather_2011.tail())
print(weather_2011.dtypes)


rental_weather_2011 = pd.merge (weather_2011, rentals_2011, on="day") #junta los dos en uno

reset -f

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
rentals_2011_weather = pd.read_csv ("weatherrentals.csv")
del rentals_2011_weather ["dteday_y"] #esto lo que hace es borrar una columna
del rentals_2011_weather ["index_y"]

rentals_2011_weather.rename(columns={"dteday_x" : "dteday"}) #RENOMBRAR

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
rentals_weather_2012 = pd.read_csv ("rentals_weather_2012.csv")

rentals_weather_11_12 = rentals_2011_weather.append(rentals_weather_2012) #UNIR POR ABAJO



wbr=rentals_weather_11_12 #SIMPLIFICAR NOMBRE DATA FRAME
del(rentals_2011_weather)
del(rentals_weather_2012)

mytable = wbr.groupby(["weathersit"]).size()

print(mytable)

n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)
print(mytable3)

bar_list = ["Sunny", "Clouddy", "Rainy"]
plt.bar(bar_list, mytable2)
plt.title("Figure 1, Percentage of weather situation")
plt.text(1.7, 50, "n: 731")

reset -f


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep= ";", decimal = ",")
wbr.shape
print(wbr.tail)
print(wbr.describe())
###############################################################################

#Sesion 4 y 5

##############################################################################
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep= ";", decimal = ",")

my_vars=["temp_celsius" , "cnt"]

wbr_minimal = wbr[my_vars]

mytable = wbr.groupby(["yr"]).size()
print(mytable)

n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

wbr_2011 = wbr[wbr.yr == 0] #subseting
plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()

wbr_2012 = wbr[(wbr.yr == 1) & (wbr.season == 1)] #susbseting with 2 variables (acordarse de poner los parentesis entre el &, porque si no no funciona)
plt.hist(wbr_2012.cnt)
wbr_2012.cnt.describe()

wbr_wint_fall = wbr[(wbr.season == 1) | (wbr.season == 4)] #susbseting with 2 variables (acordarse de poner los parentesis entre el |, porque si no no funciona)
plt.hist(wbr_wint_fall.cnt)
wbr_wint_fall.cnt.describe()

reset -f

###########################################################################


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
wbr_ue = pd.read_csv ("wbr_ue.csv", sep= ";", decimal = ",")

plt.hist(wbr_ue.temp_celsius)
wbr_ue.temp_celsius.describe()

wbr_ue["temp_celsius_c"] = wbr_ue.temp_celsius.replace(99,np.nan)
wbr_ue.temp_celsius_c.describe()
plt.hist(wbr_ue.temp_celsius_c)

reset -f
##############################################################################

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from pandas.api.types import CategoricalDtype
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir ("C:\EDEM\PEP\code_and_data")
print(os.getcwd())
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep= ";", decimal = ",")

wbr["cs_ratio"] = (wbr.casual)/(wbr.registered)
wbr.cs_ratio.describe
plt.hist(wbr.cs_ratio)

del (wbr["cnt"])
wbr ["cnt"] = wbr.casual + wbr.registered

#recodificar una variable! (IMPORTANTE)
# 1 =invie, 2= prim, 3 =veran, 4 =otoño

wbr.loc [(wbr["season"] == 1), "season_cat"] = "Winter" #loc es de location
wbr.loc [(wbr["season"] == 2), "season_cat"] = "Spring"
wbr.loc [(wbr["season"] == 3), "season_cat"] = "Summer"
wbr.loc [(wbr["season"] == 4), "season_cat"] = "Fall"

# de la columna season, cambia todos los que sale a 1 a una nueva columna (season_cat) por winter

#quality control
pd.crosstab(wbr.season, wbr.season_cat) #se sabe cuantos hay de cada uno ligado  a dos columnas

wbr.loc [(wbr["cnt"]<2567), "cnt_cat2"] = "1: Low rentals"
wbr.loc [((wbr["cnt"]>=2567) & (wbr["cnt"]<6442)), "cnt_cat2"] = "2: Average rentals"
wbr.loc [(wbr["cnt"]>=6442), "cnt_cat2"] = "3: High Rentals"

plt.scatter(wbr.cnt, wbr.cnt_cat2)

mytable = pd.cosstab (index = wbr ["cnt_cat2"], clumns = "count")
print (mytable)


#############################################################################

bar_list = ["1: Low rentals","2: Average rentals","3: High Rentals"]
mytable = wbr.groupby(["cnt_cat2"]).size()
print(mytable)

n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

plt.bar(bar_list, mytable2)

##
wbr.loc [(wbr["cnt"]<2567), "cnt_cat3"] = "Low rentals"
wbr.loc [((wbr["cnt"]>=2567) & (wbr["cnt"]<6442)), "cnt_cat3"] = "Average rentals"
wbr.loc [(wbr["cnt"]>=6442), "cnt_cat3"] = "High rentals"

bar_list = ["Low rentals","Average rentals","High Rentals"]
mytable = wbr.groupby(["cnt_cat3"]).size()
print(mytable)

n=mytable.sum()
mytable3 = (mytable/n)*100
print(mytable3)

plt.bar(mytable.index, mytable3)

##el orden de lo que pones en la tabla es importante. Es orden alfabetico
##

wbr.dtypes #tipos de datos que hay en cada variable

#se pilla esta libreria de panda para hacer las categorias
from pandas.api.types import CategoricalDtype

# First define a specific categorical data type specific for us!!! (in two sub-steps)
# Step 1: declare the ordered categories # lista ordenada de la cateogria
my_categories=["Low rentals", "Average rentals", "High rentals"]
#Step 2: Define new data type
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True) # hacemos nuevos datos que los datos son de CategoricalDtype y los datos es lo q ue esta en brackets. Importante decir que la lista es true para que este ordenada.
# Second create a new categorical_ordered variable using our specific data type
wbr["cnt_cat4"] = wbr.cnt_cat3.astype(my_rentals_type)
#Then when you plot the variable or include it in further analyses, the categories will show up 
# in your desired order
mytable = wbr.groupby(["cnt_cat4"]).size()
print(mytable)

n=mytable.sum()
mytable3 = (mytable/n)*100
print(mytable3)

plt.bar(mytable.index, mytable3)

###########################################################################################################################################################################


#SESION 5

############################################################################################################################################################################

mytable = pd.crosstab(index=wbr["workingday"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])


#T Test
#Descriptive comparison:
wbr.groupby('workingday').cnt.mean()
#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_wd=wbr.loc[wbr.workingday== 1, "cnt"]
cnt_nwd=wbr.loc[wbr.workingday== 0, "cnt"] 
#Perform a t test for mean comparison

import scipy.stats as stats
res =stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
print(res[1])

# pvalue es la probabilidad de que no haya y ninguna diferencia entree lso dos grupos que estamos observando

#CI meanplot
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="workingday", y="cnt", data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed',color="green")
props = dict(boxstyle="round", facecolor = "white", lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')


#Plotmeans
plt.figure(figsize=(5,5))
ax=sns.pointplot(x="yr",y="cnt",data=wbr,ci=95,join=0)
ax.set_ylabel('')
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed',color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.xticks((0,1), ("2011", "2012"))
plt.xlabel('Year')
plt.title('Figure 7. Average rentals by Year.''\n')
plt.text(-0.35,5400,'Mean:4504.3''\n''n:731' '\n' 't:18.6' '\n' 'Pval.: 0.000',bbox=props)

##Descriptive comparison
wbr.groupby('weathersit').cnt.mean()
#Statistical comparison
cnt_sunny=wbr.loc[wbr.weathersit==1, "cnt"]
cnt_cloudy=wbr.loc[wbr.weathersit==2, "cnt"]
cnt_rainy=wbr.loc[wbr.weathersit==3, "cnt"]
res = stats.f_oneway(cnt_sunny, cnt_cloudy,cnt_rainy )
print (res)
print("F: ", round(res[0],3), "P: " ,round(res[1],3))

#Graphic comparison: confidence intervals for the means
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="weathersit", y="cnt", data=wbr, capsize=0.05, ci=99.9, join=0)
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed',color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06' '\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Average rentals by Weather Situation.''\n')

ax= sns.boxplot(x="weathersit", y="cnt", data=wbr)




























