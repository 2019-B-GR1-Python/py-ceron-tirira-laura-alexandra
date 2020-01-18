# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:55:28 2020

@author: Laura
"""

import pandas as pd
import numpy as np

titulo=[1, 2, 3]
link_img=[4, 5, 6]
precio= [7, 8, 9]

df4=pd.DataFrame(titulo)

df4[1]=  link_img

df4[2]=  precio

df4.columns = ['Titulo','Precio','Imagen']

df2 = pd.DataFrame(np.array([titulo, link_img, precio]),columns=['titulo', 'imagen', 'precio'])
                    
pathGuardado ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\04-scrapy\\03-arania-basica\\Data\\Scrapy.csv"

df2.to_csv(pathGuardado)

df2.to_pickle(pathGuardado)
df3 = pd.read_pickle(pathGuardado)