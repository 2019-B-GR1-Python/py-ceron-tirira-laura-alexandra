# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:14 2019

@author: Laura
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

path_divorcios ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\Informe-Proyecto1\\Data\\EDV_2018.csv"
df_div = pd.read_csv(path_divorcios, delimiter=';')
df_divorcios = pd.DataFrame(data=df_div)
#Número de divorcios por provincia
#reemplazar datos.
df_divorcios.hijos_hom = df_divorcios.hijos_hom.replace({99: 0})
df_divorcios.hijos_muj = df_divorcios.hijos_muj.replace({99: 0})
#Analisis de datos
df18= df_divorcios['prov_insc'].value_counts()
df19= df18.reset_index() 
datos_provincia = df19.rename(columns={'index':'Provincia','prov_insc':'Divorcios'})
#Prepar los datos
provincia = (datos_provincia["Provincia"]).tolist()
divorcio = (datos_provincia["Divorcios"]).tolist()
#graficar
plt.figure(figsize=(50,15))
plt.pie(divorcio, labels=provincia, autopct='%1.1f%%', shadow=True)
plt.title("Divorcios por provincia", bbox={"facecolor":"0.8", "pad":5})

#cantidad de divorcios por año

#analisis de datos
df21= df_divorcios['anio_div'].value_counts()
df22= df21.reset_index() 
datos_anio = df22.rename(columns={'index':'Anio','anio_div':'Divorcios'})
#preparar los datos
x= np.array(datos_anio['Anio'])
y=np.array(datos_anio['Divorcios'])
#graficar
plt.plot(x,y)
plt.xlabel('Año')
plt.ylabel('Cantidad Divorcios')
plt.title("Cantidad de divorcios por año")
plt.fill_between(x,y,0,color="pink")
plt.axis([1984, 2020, 0, 21000])
plt.show()

#causa de divorcio
#analsis de datos
df23= df_divorcios['cau_div'].value_counts()
df24= df23.reset_index() 
datos_causa = df24.rename(columns={'index':'Causa','cau_div':'Divorcios'})
#preparar los datos
height = datos_causa['Divorcios']
bars = datos_causa['Causa']
#graficar Datos
y_pos = np.arange(len(bars))
plt.xlabel('Cantidad Divorcios')
plt.title("Cantidad de divorcios por causa")
plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.show()

#Divorcios por nivel instruccion hombre y mujeres
#analisis de datos
df25= df_divorcios['niv_insth'].value_counts()
df26= df_divorcios['niv_instm'].value_counts()
#preparar los datos
df30= df25.reset_index() 
datos_ih = df30.rename(columns={'index':'Instrucion','niv_insth':'Hombres'})
df31= df26.reset_index() 
datos_im = df31.rename(columns={'index':'Instrucion','niv_instm':'Mujeres'})
orden=[5,7,3,4,2,8,9,10,6,1,11]
serie_a= pd.Series(orden)
datos_ih["orden"] = serie_a
df_ih = datos_ih.sort_values('orden')
datos_im["orden"] = serie_a
df_im = datos_im.sort_values('orden')
datos_ins = pd.merge(df_ih, df_im, on='orden')
#graficar
instruccion = datos_ins["Instrucion_x"]
hombres_i = np.array(datos_ins["Hombres"])
mujeres_i = np.array(datos_ins["Mujeres"])
ind = [x for x, _ in enumerate(instruccion)]
plt.figure(figsize=(10,15))
plt.bar(ind, mujeres_i, width=0.8, label='Mujeres', color='silver', bottom=hombres_i)
plt.bar(ind, hombres_i, width=0.8, label='Hombres', color='gold')
plt.xticks(ind, instruccion)
plt.ylabel("Cantidad")
plt.xlabel("Instrucción")
plt.legend(loc="upper right")
plt.title("Divorcios de hombres y mujeres por instrucción")
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


#duracion del matrimonio
#analisis de datos
df12= df_divorcios['dur_mat'].value_counts()
df13= df12.reset_index() 
df_dm = df13.rename(columns={'index':'numero_anios','dur_mat':'duracion_matrimonio'})
datos_dm = df_dm.sort_values('numero_anios')
#graficar
plt.figure(figsize=(18,10))
lista1 = datos_dm["duracion_matrimonio"].tolist()
plt.title("Duración del matrimonio")
plt.xlabel("Duración matrimonio (Años)")
plt.ylabel("Número de matrimonios")
indice = np.arange(70)
plt.xticks(indice,np.array(datos_dm["numero_anios"]))  
plt.plot(lista1, 'o-')
plt.axis([0, 67, 0, 1300])
plt.show()

#numero de hijos a cargo segun la causa del divorcio
#limpieza de datos
df_divorcios.hijos_hom = df_divorcios.hijos_hom.replace({99: 0})
df_divorcios.hijos_muj = df_divorcios.hijos_muj.replace({99: 0})
#analisis de datos
df_divorcios["suma_hijos"]=df_divorcios["hijos_hom"] + df_divorcios["hijos_muj"]
df14 = df_divorcios.groupby('cau_div')['suma_hijos'].sum()
df15= df14.reset_index() 
df_hc = df15.rename(columns={'cau_div':'causa','suma_hijos':'numero_hijos'})
datos_hc = df_hc.sort_values('numero_hijos')
#graficar
x = np.array(datos_hc["causa"])
y = np.array(datos_hc["numero_hijos"])
plt.figure(figsize=(10,6))
plt.plot(x, y, 'rs')
plt.title("Número de hijos segun la causa de divorcio")
plt.setp(plt.gca().get_xticklabels(), rotation=60, horizontalalignment='right')
plt.show()

