# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:34 2019

@author: Laura
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

dt1=pd.DataFrame(arr_pand)
s1=dt1[0]
s2=dt1[1]
s3=dt1[2]

s1[0]

lista_numeros=[11,22]

serie_a= pd.Series(lista_numeros)

dt1[3] = lista_numeros

dt1[4] = s1 * s2


datos_fisicos1 = pd.DataFrame(arr_pand, columns=['Estatura (cm)', 'Peso (kg)','edad(anios)'])

datos_fisicos2 = pd.DataFrame(arr_pand, columns=['Estatura (cm)', 'Peso (kg)','edad(anios)'], index = ['Laura','Alex'])


dt1.index = ['Laura','Alex']

dt1.index = ['L','A']
dt1.columns = ['A','B','C','D','E']








