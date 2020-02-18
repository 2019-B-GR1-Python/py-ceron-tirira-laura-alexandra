import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from arania_farmacia.items import ProductoFarmacia
from scrapy.loader.processors import TakeFirst


class AraniaFarmacia(CrawlSpider):
    name = 'arania_farmacia' # Heredado (override)
    allowed_domains = [ # Heredado (override)
        'fybeca.com'
    ]

    start_urls = [ # Heredado (override)
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
    ]
   
    regla_uno = ( ## BUSQUE TODO! 
        Rule( LinkExtractor(), callback='parse_page'),
    )

    url_segmento_permitido = (
        'page'
    )

    regla_dos = ( ## Busca dentro de los dominios
        Rule(     ## permitidos y segmentos permitidos
            LinkExtractor(
                allow_domains=allowed_domains,
                allow = url_segmento_permitido
            ), callback='parse_page'
        ),
    )

   
    rules = regla_dos #regla_tres # Heredado (override)
    #def parse_page(self, response): def parse(self, response):

    def parse_page(self, response):       
        categoria= response.css('div.breadcrumb > a::text').extract()       
        tiene_categoria = False
        #if "Medicinas " in categoria:
        #    tiene_categoria = True
        #if "Salud " in categoria:
        #    tiene_categoria = True
        #if "Bebés y futura mamá " in categoria:
        #    tiene_categoria = True
        #if "Belleza " in categoria:
        #    tiene_categoria = True
        if "Cuidado personal " in categoria:
            tiene_categoria = True

        #print(tiene_categoria)

        if (tiene_categoria):
            productos = response.css('div.product-tile-inner')
            #cat = response.css('div.breadcrumb > a') .extract()           
            for producto in productos:            
                detalles = producto.css('div.detail')
                tiene_detalle = len(detalles) > 0
                if(tiene_detalle):                    
                    producto_loader =ItemLoader(item = ProductoFarmacia(),selector = producto)
                    producto_loader.default_output_processor = tuple # TakeFirst()                    
                    producto_loader.add_css('titulo','a.name::text')
                    producto_loader.add_xpath('imagen','div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')    
                    producto_loader.add_css('precio', 'div.detail > div.side > div.price::attr(data-bind)')                 
                    producto_loader.add_css('categoria','a::text')
                    producto_loader.add_css('farmacia','a::text')                    
                    yield producto_loader.load_item()



       