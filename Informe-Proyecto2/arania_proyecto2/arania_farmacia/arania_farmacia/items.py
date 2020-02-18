# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def transformar_url_imagen(texto):    
    url_fybeca = 'https://www.fybeca.com'
    cadena_texto ='../..'
    return texto.replace(cadena_texto, url_fybeca)

def transformar_precio(texto):    
    precio=""
    if len(texto) == 42:
        precio = texto[12:16]
    elif len(texto) == 43:
        precio = texto[12:17]  
    return precio

def transformar_categoria(texto):   
    return "Cuidado personal"       

def transformar_farmacia(texto):     
    return "Fybeca"    

def transformar_categoria3(texto):
    print("categoria 3") 
    return "cat3"     

class ProductoFarmacia(scrapy.Item):    
    titulo = scrapy.Field()
    imagen = scrapy.Field(input_processor = MapCompose(transformar_url_imagen), output_processor = TakeFirst())
    precio = scrapy.Field(input_processor = MapCompose(transformar_precio), output_processor = TakeFirst())
    categoria = scrapy.Field(input_processor = MapCompose(transformar_categoria), output_processor = TakeFirst())
    farmacia = scrapy.Field(input_processor = MapCompose(transformar_farmacia), output_processor = TakeFirst())
    
class AraniaFarmaciaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
