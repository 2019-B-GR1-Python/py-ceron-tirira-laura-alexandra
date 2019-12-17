# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:57 2019

@author: Laura
"""

import pandas as pd

pathGuardadoCompleto ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\03-pandas\\Data\\artwork_dataGuardadoCompleto.pickle"
df = pd.read_pickle(pathGuardadoCompleto)

##obtener nombres de los artistas.

serie_artistas_repetidos=df['artist']

artistas  = pd.unique(serie_artistas_repetidos)

artistas.size

len(artistas)

blake = df['artist'] == "Blake, William"

blake.value_counts()

df["artist"].value_counts()

df_bake =df[blake]