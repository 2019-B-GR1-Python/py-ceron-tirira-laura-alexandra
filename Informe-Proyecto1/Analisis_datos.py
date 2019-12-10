# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import matplotlib.pyplot as plt

path_matrimonios ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\Informe-Proyecto1\\Data\\EMA_2018.csv"
path_divorcios ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\Informe-Proyecto1\\Data\\EDV_2018.csv"
#df = pd.read_csv(path_matrimonios, error_bad_lines=False, encoding='utf-8')
#df = pd.read_csv(path_matrimonios, error_bad_lines=False, encoding='utf-8',  nrows=1, delimiter=';')
#3675
#cargar los archivos
df_matrimonios = pd.read_csv(path_matrimonios, delimiter=';')

df_divorcios = pd.read_csv(path_divorcios, delimiter=';')

df = pd.DataFrame(data=df_matrimonios)

#reemplazar datos.
df.hijos_rec = df.hijos_rec.replace({99: 0})

df.nmatanth = df.nmatanth.replace({99:0})

df.nmatantm= df.nmatantm.replace({99:0})

df.anio_nach= df.anio_nach.replace({9999:0})

#edad promedio de matrimonios

df2= df['edad_hom'].value_counts()

df3 = df.groupby('edad_hom')['edad_hom'].count()
df4 = df.groupby('edad_muj')['edad_muj'].count()


# unir las series.
df6=pd.concat([df3, df4], axis=1)

df6.edad_muj = df6.edad_muj.replace({None: 0})

indice = df6(df6.index)

#graficar

df6.groupby('class').mean().loc[:,['edad_hom','edad_muj']].plot(kind='bar')
plt.show()


#df5= pd.merge(df3, df4 , on='')



#df5 = pd.series

#fedata.groupby('class').mean().loc[:,['ciudad','autovia']].plot(kind='bar')
#plt.show()


#df2= df.groupby(['edad_hom']).sum().loc[:,['edad_hom','edad_muj']]
#.plot(kind='bar')
#plt.show()
#.loc[:,['edad_hom','edad_muj']]


#CONVERTIR EL INDICE EN COLUMNA

dt_Convertir= dt1.reset_index() 

