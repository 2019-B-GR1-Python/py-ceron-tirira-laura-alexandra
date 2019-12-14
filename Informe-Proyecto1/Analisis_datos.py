# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

path_matrimonios ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\Informe-Proyecto1\\Data\\EMA_2018.csv"
#Numero de Matrimonios de hombres y mujeres por edades.

#cargar los archivos
df_matrimonios = pd.read_csv(path_matrimonios, delimiter=';')
df = pd.DataFrame(data=df_matrimonios)

#reemplazar datos (limpiar datos).
df.hijos_rec = df.hijos_rec.replace({99: 0})
df.nmatanth = df.nmatanth.replace({99:0})
df.nmatantm= df.nmatantm.replace({99:0})
df.anio_nach= df.anio_nach.replace({9999:0})
#edad promedio de matrimonios(analisis de datos)
df3 = df.groupby('edad_hom')['edad_hom'].count()
df4 = df.groupby('edad_muj')['edad_muj'].count()
# prepar los datos
df6=pd.concat([df3, df4], axis=1)
df6.edad_muj = df6.edad_muj.replace({None: 0})
df7= df6.reset_index() 
datos_edad = pd.DataFrame(df7, columns=['Edad', 'Hombres','Mujeres'])
datos_edad = df7.rename(columns={'index':'Edad','edad_hom':'Hombres','edad_muj':'Mujeres'})
datos_hombres = datos_edad["Hombres"].tolist()
datos_mujeres= datos_edad["Mujeres"].tolist()
datos_edad_grafico= datos_edad["Edad"].tolist()
datos= [datos_hombres,datos_mujeres] 
#graficar
X = np.arange(81)
plt.figure(figsize=(50,10))
pl.xlabel('Edad')
pl.ylabel('Cantidad')
pl.title('Matrimonios de hombres y mujeres por edades') 
plt.bar(X + 0.00, datos[0], color = "b", width=0.25, label='Hombres')
plt.bar(X + 0.25, datos[1], color = "r", width=0.25, label='Mujeres')
plt.xticks(X +0.10, datos_edad_grafico)
plt.axis([0, 85, 0, 3700])
plt.legend()

 
#Numero de matromonios por meses
#Analisis de datos
df8= df['mes_insc'].value_counts()
df9= df8.reset_index() 
datos_mes = df9.rename(columns={'index':'Mes','mes_insc':'Matrimonios'})
#preparar los datos
orden=[12,8,3,10,11,7,2,4,5,9,6,1]
serie_a= pd.Series(orden)
datos_mes["orden"] = serie_a
mes_dat = datos_mes.sort_values('orden')
mes = np.array(mes_dat["Mes"])
matrimonios = np.array(mes_dat["Matrimonios"])
#graficar
X = mes
Y = matrimonios
plt.figure(figsize=(12,10))
plt.scatter(X, Y, s=100, alpha=0.5)


#estado civil del hombre anterior a casarse
#Analisis de datos
#hombres
df10= df['est_civih'].value_counts()
df11= df10.reset_index() 
datos_ech = df11.rename(columns={'index':'estado_civil','est_civih':'Matrimonios'})
#mujeres
df12= df['est_civim'].value_counts()
df13= df12.reset_index() 
datos_ecm = df13.rename(columns={'index':'estado_civil','est_civim':'Matrimonios'})
#preparar los datos
x = datos_ech["estado_civil"]
y = datos_ech["Matrimonios"]
xm = datos_ecm["estado_civil"]
ym = datos_ecm["Matrimonios"]
#graficar primero
#plt.figure()
plt.plot(x, y, color="blue", linewidth=2.5, linestyle="-")
plt.subplot(1,2,1)
plt.plot(x,y)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.setp(plt.gca().get_yticklabels(), rotation=45, horizontalalignment='right')
plt.subplot(1,2,2)
#graficar el segundo
plt.plot(xm,ym, color="orange", linewidth=2.5, linestyle="-")
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.setp(plt.gca().get_yticklabels(), rotation=45, horizontalalignment='right')


#matrimonios por provincia

df16= df['prov_insc'].value_counts()
df17= df16.reset_index() 
datos_dp = df17.rename(columns={'index':'Provincia','prov_insc':'Matrimonios'})
#preparar los datos
provincia_d = np.array(datos_dp["Provincia"])
divorcios_d = np.array(datos_dp["Matrimonios"])
#graficar
X = provincia_d
Y = divorcios_d
plt.figure(figsize=(23,10))
plt.bar(X, Y, color="pink")
plt.title("Matrimonios por provincia")
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

