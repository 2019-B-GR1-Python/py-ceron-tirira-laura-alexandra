import scrapy
import pandas as pd
import numpy as np

class IntroSpider(scrapy.Spider):
    name='introduccion_spider'
    titulos=[]
    precios=[]
    url_imagenes=[]


    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
     'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
     'http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
     'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
     'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html',
     'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
     'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
     'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
     'http://books.toscrape.com/catalogue/category/books/romance_8/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
     'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
     'http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html',
     'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
     'http://books.toscrape.com/catalogue/category/books/childrens_11/page-2.html'
     'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html',
     'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html',
     'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-4.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-4.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-5.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-6.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-7.html',
     'http://books.toscrape.com/catalogue/category/books/default_15/page-8.html',
     'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
     'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
     'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html', 
     'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-4.html',    
     'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
     'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
     'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
     'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-3.html',
     'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
     'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
     'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
     'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
     'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
     'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
     'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
     'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
     'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
     'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
     'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
     'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
     'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html',
     'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
     'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
     'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
     'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
     'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
     'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
     'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
     'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
     'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
     'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
     'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
     'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
     'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
     'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
     'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
     'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
     'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
     'http://books.toscrape.com/catalogue/category/books/crime_51/index.html'
    
    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        #titulos
        titulo = etiqueta_contenedora.css('h3 > a::text').extract()
        for t in titulo:
            self.titulos.append(t)
        #print(titulo)
        
        #link imagen
        link_imagen = etiqueta_contenedora.css('div.image_container > a::attr(href)').extract()
        #link_imagen_completo=[]
        for l in link_imagen:            
            l = 'http://books.toscrape.com/catalogue' + l[8:]
            self.url_imagenes.append(l)
            #link_imagen_completo.append(l)
      
        #print(link_imagen_completo)  

        #precios
        precio = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        #print(precio)
        #precios_nuevos = []
        for p in precio:                                   
            pr=float(p[1:])          
            self.precios.append(pr)
            #precios_nuevos.append(pr)
        
        #print(precios_nuevos)

        #lista de links de los libros
        link_libros = response.css('ul > li > ul> li> a::attr(href)').extract()
        #link_libros_completos =[]
        for lb in link_libros:            
            if(lb == "index.html"):
                lb= '../travel_2/index.html'
                        
            lb = 'http://books.toscrape.com/catalogue/category/books' + lb[2:]
            #link_libros_completos.append(lb)            

        #print(link_libros_completos)

       # self.urls.append('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')


        print('titulos t', len(self.titulos))
        print('precios t', len(self.precios))
        print('img link t', len(self.url_imagenes))

        #GUARDAR DATOS
        df2 = pd.DataFrame(self.titulos)
        df2[1]=self.precios
        df2[2]=self.url_imagenes# link_imagen_completo
        df2.columns=['Titulo', 'Precio', 'Imagen']

        #print(df2)
        
        pathGuardadoCSV ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\04-scrapy\\03-arania-basica\\Data\\Scrapy.csv"
        pathGuardadoPC ="C:\\Users\\Laura\\Documents\\GitHub\\py-ceron-tirira-laura-alexandra\\04-scrapy\\03-arania-basica\\Data\\ScrapyPC.pickle"
        df2.to_csv(pathGuardadoCSV)
        df2.to_pickle(pathGuardadoPC)

         




        
#para ejecutar
#scrapy crawl introduccion_spider
