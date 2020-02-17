# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:24:11 2020

@author: Laura
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

path_productos ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\Informe-Proyecto2\\Data\\productosFarmaceuticos.json"

df_productos = pd.read_json(path_productos)
df = pd.DataFrame(df_productos)


categorias = df.categoria.value_counts()



df1 = df.groupby(['farmacia','categoria'])['categoria']#.count()
d = df1.groups()

df2 = df.groupby('categoria').values_count()

df1 = df.groupby(['farmacia','categoria'])['categoria'].count()
a= df2.first()
#['categoria'].sum()


df2 = df.groupby('edad_muj')['edad_muj'].count()

b= df.groupby('farmacia')['categoria'].sum().to_frame().reset_index() Bebes y futura mama