# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:34 2019

@author: Laura
"""

import pandas as pd
import numpy as np


pathGuardadoCompleto ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_dataGuardadoCompleto.pickle"
df = pd.read_pickle(pathGuardadoCompleto)

df2 = df.set_index('id')

"""
        nota 1 disiplina
pepito    7      5
juanira   8      9
maria     9      2

"""

datos={"nota 1" :{
        "Pepito": 7,
        "Juanita":8,
        "Maria":9},
        "disciplina":{ "Pepito": 5,
        "Juanita":9,
        "Maria":2}}




notas = pd.DataFrame(datos)

type(notas.loc["Pepito"]) #serie

notas.loc["Pepito","disciplina"]

notas.loc["Pepito", ["disciplina", "nota 1"]]

notas.loc[["Pepito","Juanita"], ["nota 1"]]



condicion_nota =notas["nota 1"] > 7

mayores_siete = notas.loc[condicion_nota]

#dos condiciones.
condicion_disciplina =notas["disciplina"] > 7

mayores_siete_nota_disciplina = notas.loc[condicion_nota][condicion_disciplina]

mayores_siete_nota_disciplina = notas.loc[condicion_nota ,["nota 1"]

##notas
##mayores_siete[condicion:disc]

notas.loc["Maria", "disciplina"] = 7

#Estudiantes  menores a 7 en disciplina

menores_siete = notas["disciplina"] < 7

disciplina = notas.loc[menores_siete]

##disciplina_1 = notas.loc[["disciplina"] < 7 ],"disciplina"] = 7

# solo a pepito se le va a poner 10 en todo

##disciplina se les baje a 7

notas.loc[:, "disciplina"] =7

##añadir la columna promedio nota1 y disciplina











