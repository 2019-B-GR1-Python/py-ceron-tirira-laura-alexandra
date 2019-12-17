# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:41 2019

@author: Laura
"""
import pandas as pd
import numpy as np
import os
import sqlite3

pathGuardadoCompleto ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_dataGuardadoCompleto.pickle"
df5 = pd.read_pickle(pathGuardadoCompleto)

df =df5.iloc[49980:50019,:].copy()


#tipos de archivos
#json
#excel
#sql

####excel####

path_guardado='C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index=False)

columnas =['artist','title','year']

df.to_excel(path_guardado,columns=columnas)

#multimples hojas de trabajo #####

path_multiple='C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\mi_df_multiple.xlsx'

writer = pd.ExcelWriter(path_multiple, engine='xlsxwriter')

df.to_excel(writer, sheet_name='Primera')
df.to_excel(writer, sheet_name='Segunda', index= False)
df.to_excel(writer, sheet_name='Tercera', columns=columnas)

writer.save()

#####
num_artistas=df['artist'].value_counts()

path_colores='C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\mi_df_colores.xlsx'

writer = pd.ExcelWriter(path_colores, engine='xlsxwriter')

num_artistas.to_excel(writer, sheet_name='Artistas')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index) +1)

formato_artistas = {
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type":"percentile"}

hoja_artistas.conditional_format(rango_celdas,formato_artistas)
writer.save()


####   SQl   #######

with sqlite3.connect("bdd_artist.db") as conexion:
    df5.to_sql('py_artistas', conexion)


## whith mysql.connect('mysql://user.password@ip:puerto/nombre_base')
#se exporta en fromato complejo
df.to_json('artistas.json')

df.to_json('artistas.json', orient='table')








