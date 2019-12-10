# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd


#11) #11) ¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista= pd.Series(mylist)
serie_arreglo= pd.Series(myarr)
serie_diccionario= pd.Series(mydict)


##12 ¿Como convertir el indice de una serie en una columna de un DataFrame?
ser = pd.Series(mydict) 
dt1=pd.DataFrame(ser)

dt_Convertir= dt1.reset_index() 


#13) ¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df2=pd.concat([ser1, ser2], axis=1)


#14

#15) 

#16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser5 = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
contador= ser5.value_counts()


#17) 


#18) 


#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser4 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
posicion= pd.Series(ser4, index=pos)

#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser6 = pd.Series(range(5))
ser7 = pd.Series(list('abcde'))

#vertical
df6=pd.concat([ser6, ser7], axis=1)

#horizontal
df7=pd.concat([ser6, ser7], axis=0)


#21)

#22)¿Como importar solo columnas especificas de un archivo csv?

path ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_data.csv"

columnas =['id','artist','medium','year',
           'acquisitionYear','height',
           'width','units']
df8 = pd.read_csv (path, nrows=10, usecols=columnas)













