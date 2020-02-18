# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def transformar_url_imagen(texto):      
    return " "

def transformar_precio(texto):
    #print("precio")     
    indice = texto.find('PVP')
    #print("indice",indice) 
    precio=""   
    if(indice==0):
        precio=texto[6:]
        #("precio", precio)    
    return precio.strip()
    

def transformar_titulo(texto):
    print("titulo en los items")
    print(texto)
    indice = texto.find('PVP')    
    print("indice",indice)    
    return texto   

def transformar_categoria(texto):   
    return "Vitaminas"       

def transformar_farmacia(texto):     
    return "Pharmacys"      

class ProductoPharmacys(scrapy.Item):        
    titulo = scrapy.Field(input_processor = MapCompose(transformar_titulo), output_processor =  TakeFirst())
    imagen = scrapy.Field(input_processor = MapCompose(transformar_url_imagen), output_processor = TakeFirst())
    precio = scrapy.Field(input_processor = MapCompose(transformar_precio), output_processor = TakeFirst())
    categoria = scrapy.Field(input_processor = MapCompose(transformar_categoria), output_processor = TakeFirst())
    farmacia = scrapy.Field(input_processor = MapCompose(transformar_farmacia), output_processor = TakeFirst())


class AraniaPharmacysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
