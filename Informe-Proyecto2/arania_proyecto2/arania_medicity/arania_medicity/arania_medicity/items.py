# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def transformar_url_imagen(texto):
    #print("imagen")        
    url_medicity = 'https://www.farmaciasmedicity.com'
    #print(url_medicity + texto)    
    return url_medicity+texto

def transformar_precio(texto):  
    #print("precio")  
    #print(texto)
    return texto

def transformar_titulo(texto):
    #print("titulo en los items")
    #print(texto)
    #print('tamanio: ', len(texto))
    if not(len(texto) == 21 or len(texto) == 17):
        #print('no tit', texto)
        return texto

def transformar_categoria(texto):   
    return "Belleza"       

def transformar_farmacia(texto):     
    return "Medicity"      

class ProductoMedicity(scrapy.Item):        
    titulo = scrapy.Field(input_processor = MapCompose(transformar_titulo), output_processor =  TakeFirst())
    imagen = scrapy.Field(input_processor = MapCompose(transformar_url_imagen), output_processor = TakeFirst())
    precio = scrapy.Field(input_processor = MapCompose(transformar_precio), output_processor = TakeFirst())
    categoria = scrapy.Field(input_processor = MapCompose(transformar_categoria), output_processor = TakeFirst())
    farmacia = scrapy.Field(input_processor = MapCompose(transformar_farmacia), output_processor = TakeFirst())

class AraniaMedicityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
