# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:30:34 2020

@author: Laura
"""
import numpy as np
import pandas as pd
import string
import random

#1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros.

arr_pand = np.random.randint(1,10,60).reshape(10,6)
dt1=pd.DataFrame(arr_pand)
primeros_5 = dt1[:5]
ultimos_5 = dt1[5:]

#2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

arr = np.random.randint(0,10,24).reshape(6,4)
dt2=pd.DataFrame(arr)
dt2.rename(columns={0: 'A', 1: 'B',2:'C',3:'D'}, inplace=True)
fecha = ['2013-01-01','2013-01-02','2013-01-03','2013-01-04','2013-01-05','2013-01-06']
dt2[4] = fecha

df2= dt2.set_index(4)

#4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.
dt4=pd.DataFrame(arr_pand)

list(dt4.columns)

dt4.values

#5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

dt5=pd.DataFrame(arr_pand)
dt5.describe()

#6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

dt6=pd.DataFrame(arr_pand)
df6 = dt6.transpose()

#7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

dt7=pd.DataFrame(arr_pand)

dt7.sort_values(by=0)
dt7.sort_values(by=1, ascending=False)
dt7.sort_values(by=2)
dt7.sort_values(by=3, ascending=False)
dt7.sort_values(by=4)
dt7.sort_values(by=5, ascending=False)

#8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

dt8=pd.DataFrame(arr_pand)

df8 = dt8[:][dt8>7]

#9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

dt9=pd.DataFrame(arr_pand)

df10 = dt9[:][dt9 > 6]

dframe9 = df10.replace({np.nan:0})


#10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

dt10=pd.DataFrame(arr_pand)

media = dt10[:].mean()
mediana = dt10[:].median()
promedio = dt10[:].mean()


#11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

dt11=pd.DataFrame(arr_pand)

dframe11=pd.DataFrame(arr_pand)

dtRes11 = dt11.append(dframe11)

dtResultado= dtRes11.reset_index() 


#12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. 
#Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    lista=[]
    for i in range(stringLength):
        random.choice(letters)
        lista.append(random.choice(letters))        
    return lista

arr_str = randomString(60)
a = np.array(arr_str).reshape(10,6)
dt12=pd.DataFrame(a)

dt12[6]=dt12[0].str.cat(dt12[1])
dt12[7]=dt12[3].str.cat(dt12[4])
dt12[8]=dt12[5].str.cat(dt12[6])


#13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna

dt13=pd.DataFrame(arr_pand)

col1= dt13[0].value_counts()
col2= dt13[1].value_counts()
col3= dt13[2].value_counts()
col4= dt13[3].value_counts()
col5= dt13[4].value_counts()
col6= dt13[5].value_counts()


#14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. 
#Crear una nueva columna con el calculo por fila (A * B ) / C

arr_pand = np.random.randint(1,10,30).reshape(10,3)
dt14=pd.DataFrame(arr_pand)
dt14.rename(columns={0: 'A', 1: 'B',2:'C'}, inplace=True)
dt14[3] = (dt14['A'] * dt14['B'])/ dt14['C']













