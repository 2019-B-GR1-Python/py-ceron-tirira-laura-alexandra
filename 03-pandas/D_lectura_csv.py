# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:39 2019

@author: Laura
"""

import pandas as pd
import os

# 1) json, csv, html xml
# 2) Binary files-> 
# 3) relation databases

path ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_data.csv"

pathGuardado ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_dataModificado.pickle"

pathGuardadoCompleto ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_dataGuardadoCompleto.pickle"


df = pd.read_csv (path, nrows=10)


columnas =['id','artist','medium','year',
           'acquisitionYear','height',
           'width','units']

df2 = pd.read_csv (path, nrows=10, usecols=columnas)


df3 = pd.read_csv (path, nrows=10, usecols=columnas, index_col ='id')

#guardar archivo

df3.to_pickle(pathGuardado)


df4 = pd.read_csv(path)

df4.to_pickle(pathGuardadoCompleto)


df5 = pd.read_pickle(pathGuardadoCompleto)

