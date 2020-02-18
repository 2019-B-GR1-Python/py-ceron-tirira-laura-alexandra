import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from arania_pharmacys.items import ProductoPharmacys
from scrapy.loader.processors import TakeFirst

class AraniaMedicity(CrawlSpider):
    name = 'arania_pharmacys'
    urls = [ # Heredado (override)
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=1&mid=6',
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=3&mid=6',
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=19&mid=6',
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=13&mid=6',
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=7&mid=6',

    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

  

    def parse(self, response):      
        print('res', response)          
        productos = response.xpath('///*[@id="ctl00_ContentPlaceHolder1_dtlstProductos"]/span')        
        categoria=response.css('span.txt_titulo_prod::text').extract() #response.request.url.split('/')#response.css('ol.breadcrumb > li.active >a::text').extract()
        print('categoria: ',categoria)       
        tiene_categoria = False       
        #if "Dermocosmética" in categoria:
        #    tiene_categoria = True
        #if "Pañales" in categoria:
        #    tiene_categoria = True
        #if "Maquillaje" in categoria:
        #    tiene_categoria = True
        #if "Fórmulas Infantiles" in categoria:
        #    tiene_categoria = True
        if "Vitaminas y Minerales" in categoria:
            tiene_categoria=True
        # print(tiene_categoria)
        if(tiene_categoria):
            for producto in productos:                
                producto_loader =ItemLoader(item = ProductoPharmacys(),selector = producto)
                producto_loader.default_output_processor = TakeFirst()                               
                producto_loader.add_css('titulo', 'span.style15::text')
                producto_loader.add_css('imagen', 'span.style15::text')
                producto_loader.add_css('precio', 'span.style15::text')                 
                producto_loader.add_css('categoria','span.style15::text')
                producto_loader.add_css('farmacia','span.style15::text')                    
                yield producto_loader.load_item()
            


        


       