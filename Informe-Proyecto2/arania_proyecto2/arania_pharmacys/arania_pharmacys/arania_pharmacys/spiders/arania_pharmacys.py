import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from arania_pharmacys.items import ProductoPharmacys
from scrapy.loader.processors import TakeFirst

class AraniaMedicity(CrawlSpider):
    name = 'arania_pharmacys'
    urls = [ # Heredado (override)
        'http://www.pharmacys.com.ec/Resultado_productos.aspx?sid=1&mid=6'
    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    # start_urls = [ # Heredado (override)
    #     'https://www.farmaciasmedicity.com/shop/category/medicinas-1328'
    # ] 
     
    # allowed_domains = [ # Heredado (override)
    #     'farmaciasmedicity.com'
    # ]

    # regla_uno = ( ## BUSQUE TODO! 
    #     Rule( LinkExtractor(), callback='parse_page'),
    # )

    # url_segmento_permitido = (
    #     'category'
    # )

    # regla_dos = ( ## Busca dentro de los dominios
    #     Rule(     ## permitidos y segmentos permitidos
    #         LinkExtractor(
    #             allow_domains=allowed_domains,
    #             allow = url_segmento_permitido
    #         ), callback='parse_page'
    #     ),
    # )
   
    #rules = regla_dos

    def parse(self, response):        
        print('response',response)
        #productos = response.xpath('//div[@id="grid_list"]')
        #producto_loader.add_xpath('imagen','///*[@id="tab7"]/article/header/h2/a/@href/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')    
        productos = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_dtlstProductos"]/span')
        #print("productos")
        #print(productos.extract())



        # categoria_dato=response.request.url.split('/')#response.css('ol.breadcrumb > li.active >a::text').extract()
        # print(categoria_dato)
        # categoria = categoria_dato[5]       
        tiene_categoria = True #False       
        # if "cuidado-personal-y-belleza" in categoria:
        #    tiene_categoria = True
        # if "bebés" in categoria:
        #    tiene_categoria = True
        # if "belleza" in categoria:
        #    tiene_categoria = True
        # if "cuidado personal " in categoria:
        #    tiene_categoria = True
        # print(tiene_categoria)
        if(tiene_categoria):
            for producto in productos:
                #a = producto.css('span.style15').extract();
                #print("a", a)
                #tit = producto.xpath('//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/text()').extract()
                tit = producto.xpath('//span[@id ="ctl00_ContentPlaceHolder1_dtlstProductos"]/span/table/tr/td/table/tr/td/table/tr/td/text()').extract()
                print('titulo: ', tit)
                # producto_loader =ItemLoader(item = ProductoPharmacys(),selector = producto)
                # producto_loader.default_output_processor = TakeFirst()                               
                # producto_loader.add_xpath('titulo', 'table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/')
                # producto_loader.add_css('imagen', 'img::attr(data-zoom-image)')
                # producto_loader.add_css('precio', 'span.oe_currency_value::text')                 
                # producto_loader.add_css('categoria','span.oe_currency_value::text')
                # producto_loader.add_css('farmacia','span.oe_currency_value::text')                    
                # yield producto_loader.load_item()
            


        


       